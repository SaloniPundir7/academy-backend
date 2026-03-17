from django.contrib import admin

from django.contrib import admin
from .models import StudentProfile, TeacherProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "branch", "year")

    search_fields = ("user__username", "branch")

    list_filter = ("branch",)


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "department")

    search_fields = ("user__username", "department")

    list_filter = ("department",)
