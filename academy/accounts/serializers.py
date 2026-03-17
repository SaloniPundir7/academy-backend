from rest_framework import serializers
from .models import StudentProfile, TeacherProfile


class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = ["id", "user", "branch", "year"]


class TeacherProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherProfile
        fields = ["id", "user", "department"]