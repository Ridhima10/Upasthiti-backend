from django.urls import path, include

#? djangorestframework-simplejwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#? drf-spectacular
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView, SpectacularJSONAPIView

#? User
from user import views as UserViews

#? Auth
from authlogic import views as AuthViews

#? Attendance
from attendance import views as AttenViews

#? Classes

from classes import views as ClassViews

#? College

from college import views as CollegeViews

#? Course

from course import views as CourseViews

#? Department

from department import views as DeptViews

urlpatterns = [
    #? Auth Routes
    path('auth/token/',
         TokenObtainPairView.as_view(),
         name='obtain_token_pair'),
    path('auth/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),

    #? Schema
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/json/', SpectacularJSONAPIView.as_view(), name='json_schema'),
    path('schema/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),

    #? User
    path('user/',
         UserViews.UserListCreateAPIView.as_view(),
         name='user-list-create'),
    path('user/<int:pk>/',
         UserViews.UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-retrieve-update-destroy'),
    path('user/update_password/<int:pk>/',
         UserViews.UserPasswordUpdateAPIView.as_view(),
         name='user-password-update'),

    #? Auth
    path('auth/me/', AuthViews.AuthMeApiView.as_view(), name='auth-me'),

    #? Attendance
    path('attendance/',
         AttenViews.AttendanceListCreateAPIView.as_view(),
         name='attendance-list-create'),
    path('attendance/<int:pk>/',
         AttenViews.AttendanceRetrieveUpdateDestroyAPIView.as_view(),
         name='attendance-retrieve-update-destroy'),

    #? Classes
    path('classes/',
         ClassViews.ClassesListCreateAPIView.as_view(),
         name='Classes-list-create'),
    path('Classes/<int:pk>/',
         ClassViews.ClassesRetrieveUpdateDestroyAPIView.as_view(),
         name='Classes-retrieve-update-destroy'),

    #? College
    path('college/',
         CollegeViews.CollegeListCreateAPIView.as_view(),
         name='College-list-create'),
    path('college/<int:pk>/',
         CollegeViews.CollegeRetrieveUpdateDestroyAPIView.as_view(),
         name='College-retrieve-update-destroy'),

    #? Course
    path('course/',
         CourseViews.CourseListCreateAPIView.as_view(),
         name='Course-list-create'),
    path('course/<int:pk>/',
         CourseViews.CourseRetrieveUpdateDestroyAPIView.as_view(),
         name='Course-retrieve-update-destroy'),

    #? Department
    path('department/',
         DeptViews.DepartmentListCreateAPIView.as_view(),
         name='Department-list-create'),
    path('Department/<int:pk>/',
         DeptViews.DepartmentRetrieveUpdateDestroyAPIView.as_view(),
         name='Department-retrieve-update-destroy'),
]
