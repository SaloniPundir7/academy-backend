from rest_framework import serializers
from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "title", "description", "created_by", "created_at"]

        read_only_fields = ["created_at"]
        
class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["id", "title", "video_url", "course", "order", "duration", "is_free"]

    def validate(self, data):
        course = data.get("course")
        order = data.get("order")

        if Lesson.objects.filter(course=course, order=order).exists():
            raise serializers.ValidationError("Lesson order already exists for this course")

        return data