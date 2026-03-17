from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, MyCoursesView
from .views import CourseStatsView
from .views import CourseLessonsView

router = DefaultRouter()

router.register(r"courses", CourseViewSet)
router.register(r"lessons", LessonViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('my-courses/',MyCoursesView.as_view()),
    path("course-stats/", CourseStatsView.as_view()),
    path("course-lessons/<int:course_id>/", CourseLessonsView.as_view()),
]

