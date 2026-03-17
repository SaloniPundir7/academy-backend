from django.urls import path
from .views import create_student_profile, create_teacher_profile, get_student_profile, get_teacher_profile

urlpatterns = [

    path("student-profile/", create_student_profile),
    path("teacher-profile/", create_teacher_profile),
    path("get-student-profile/", get_student_profile),
    path("get-teacher-profile/", get_teacher_profile) 

]