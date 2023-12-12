from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from base.models import User, Course, Topic
from .serializers import UserSerializer, CourseSerializer, TopicSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import authenticate

import logging

logger = logging.getLogger(__name__)



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
        'signup/',
        'create_course/',
        'create_topic/<int:course_id>/',
        'list_courses/',
        'list_topics/<int:course_id>/',
    ]

    return Response(routes)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# New LoginView
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        

        print(f"Received credentials: username={username}, password={password}, {user}")


        if user is not None:
            # Authentication successful, proceed with token generation
            # print(f"User authenticated: {user}")
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            response_data = serializer.validated_data
            return Response(response_data, status=200)
            # ...
        else:
            # Authentication failed
            print("Authentication failed")
            return Response({'detail': 'Invalid credentials'}, status=401)


# Your existing LogoutView
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'detail': 'refresh_token is required'}, status=400)

        try:
            # Blacklist the provided refresh token
            # RefreshToken(refresh_token).blacklist()           TODO ----------------------- BLACKLIST -----------------------------------
            return Response({'detail': 'Successfully logged out'}, status=200)
        except Exception as e:
            return Response({'detail': str(e)}, status=500)

class CreateCourseView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateTopicView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        course_id = self.kwargs.get('course_id')
        course = Course.objects.get(pk=course_id)
        serializer.save(course=course)


class ListCoursesView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(user=self.request.user)


class ListTopicsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TopicSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Topic.objects.filter(course_id=course_id)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
#     user = request.user
#     notes = user.note_set.all()
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)
