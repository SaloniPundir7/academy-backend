from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Course
from .serializer import CourseSerializer
from .models import Lesson
from .serializer import LessonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from enrollments.models import Enrollment
from .permissions import IsCourseOwner
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.exceptions import PermissionDenied



def api_response(data=None, message="", status_code=status.HTTP_200_OK):
    return Response({
        "status": True,
        "status_code": status_code,
        "message": message,
        "data": data
    }, status=status_code)




class CourseViewSet(ModelViewSet):

    queryset = Course.objects.all()

    serializer_class = CourseSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]

    filterset_fields = ["created_by"]

    search_fields = ["title", "description"]
    
    def get_permissions(self):

        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsCourseOwner()]

        return [IsAuthenticated()]
    
    def list(self, request, *args, **kwargs):
        courses = self.get_queryset()
        serializer = self.get_serializer(courses, many=True)
        return api_response(serializer.data, "Courses fetched successfully")

    def retrieve(self, request, *args, **kwargs):
        course = self.get_object()
        serializer = self.get_serializer(course)
        return api_response(serializer.data, "Course fetched successfully")




class LessonViewSet(ModelViewSet):

    queryset = Lesson.objects.all()

    serializer_class = LessonSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ["course"]
    
    def get_permissions(self):
     if self.action in ["create", "update", "partial_update", "destroy"]:
        return [IsAuthenticated(), IsCourseOwner()]
     return [IsAuthenticated()]


class MyCoursesView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        enrollments = Enrollment.objects.filter(student=request.user)

        courses = [en.course for en in enrollments]

        serializer = CourseSerializer(courses, many=True)

        return api_response(serializer.data, "My courses fetched successfully")
    


class CourseStatsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        total_courses = Course.objects.count()

        total_enrollments = Enrollment.objects.count()

        my_courses = Course.objects.filter(created_by=request.user).count()

        data = {
            "total_courses": total_courses,
            "total_enrollments": total_enrollments,
            "my_courses": my_courses
        }

        return api_response(data, "Course statistics fetched successfully")
    



class CourseLessonsView(APIView):

    permission_classes = [IsAuthenticated]

    

   from rest_framework.exceptions import PermissionDenied

def get(self, request, course_id):

    lessons = Lesson.objects.filter(course_id=course_id).order_by("order")

    # Allow FREE lessons to everyone
    free_lessons = lessons.filter(is_free=True)

    # Check enrollment
    is_enrolled = Enrollment.objects.filter(
        student=request.user,
        course_id=course_id
    ).exists()

    if not is_enrolled:
        serializer = LessonSerializer(free_lessons, many=True)
        return api_response(serializer.data, "Free lessons only (not enrolled)")

    serializer = LessonSerializer(lessons, many=True)
    return api_response(serializer.data, "All lessons fetched")