from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment
from .serializer import EnrollmentSerializer


class EnrollmentViewSet(ModelViewSet):

    queryset = Enrollment.objects.all()

    serializer_class = EnrollmentSerializer

    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
      serializer.save(student=self.request.user)
