from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.title

class Lesson(models.Model):

    title = models.CharField(max_length=200)

    video_url = models.URLField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    order = models.IntegerField()

    duration = models.IntegerField(default=0, help_text="Duration in minutes")

    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.title
 