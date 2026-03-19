from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment
from .serializer import EnrollmentSerializer
from payments.models import Payment
from rest_framework.exceptions import ValidationError


class EnrollmentViewSet(ModelViewSet):

    queryset = Enrollment.objects.all()

    serializer_class = EnrollmentSerializer

    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
       user = self.request.user
       course = serializer.validated_data.get("course")

       payment_exists = Payment.objects.filter(
           user=user,
           course=course,
           status='success'
           ).exists()

       if not payment_exists:
        raise ValidationError("You must complete payment before enrolling.")

       serializer.save(student=user)
