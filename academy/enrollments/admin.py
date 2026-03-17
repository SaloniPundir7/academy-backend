from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    list_display = ("id", "student", "course", "enrolled_at", "status")

    search_fields = ("student__username", "course__title")

    list_filter = ("status", "enrolled_at")

    ordering = ("-enrolled_at",)
