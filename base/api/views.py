from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from base.models import User, Course, Topic
from .serializers import UserSerializer, CourseSerializer, TopicSerializer , MyTokenObtainPairSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import authenticate

import logging

logger = logging.getLogger(__name__)



# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         token['role'] = user.profile.role if hasattr(user, 'profile') else 'instructor'  # Assuming the role is stored in a profile model

#         # ...

#         return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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



class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Check if the username already exists
        username = request.data.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'detail': 'Username already exists. Please choose another username.'}, status=status.HTTP_400_BAD_REQUEST)

        # Continue with the user registration
        response = super().create(request, *args, **kwargs)

        # Customize the response message
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'detail': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return response


# New LoginView
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            # Password is correct, proceed with token generation
            serializer = self.serializer_class(data={"username": username, "password": password})
            serializer.is_valid(raise_exception=True)
            response_data = serializer.validated_data

            # Add additional data to the response
            response_data['role'] = user.profile.role if hasattr(user, 'profile') else 'instructor'
            
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

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
