from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import StudentProfile, TeacherProfile
from .serializers import StudentProfileSerializer, TeacherProfileSerializer


@api_view(["POST"])
def create_student_profile(request):

    serializer = StudentProfileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_teacher_profile(request):

    serializer = TeacherProfileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_student_profile(request):

    try:
        profile = StudentProfile.objects.get(user=request.user)
    except StudentProfile.DoesNotExist:
        return Response(
            {"message": "Student profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = StudentProfileSerializer(profile)

    return Response(serializer.data)

@api_view(["GET"])
def get_teacher_profile(request):

    try:
        profile = TeacherProfile.objects.get(user=request.user)
    except TeacherProfile.DoesNotExist:
        return Response(
            {"message": "Teacher profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = TeacherProfileSerializer(profile)

    return Response(serializer.data)
