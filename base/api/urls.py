from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from .views import MyTokenObtainPairView, SignupView, CreateCourseView, CreateTopicView, ListCoursesView, ListTopicsView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('signup/', SignupView.as_view(), name='signup'),
    path('create_course/', CreateCourseView.as_view(), name='create_course'),
    path('create_topic/<int:course_id>/', CreateTopicView.as_view(), name='create_topic'),
    path('list_courses/', ListCoursesView.as_view(), name='list_courses'),
    path('list_topics/<int:course_id>/', ListTopicsView.as_view(), name='list_topics'), 
]
