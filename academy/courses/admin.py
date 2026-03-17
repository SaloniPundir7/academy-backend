from django.contrib import admin
from .models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "created_by", "created_at")

    search_fields = ("title",)

    list_filter = ("created_at",)

    ordering = ("-created_at",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "course", "order")

    search_fields = ("title",)

    list_filter = ("course",)

    ordering = ("order",)
