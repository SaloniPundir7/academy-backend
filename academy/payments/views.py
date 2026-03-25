from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializer import PaymentSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_cookie

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status='success')

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # Cache retrieve (GET /payments/{id}/)
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 5))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
'''from django.core.cache import cache

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status='success')
        cache.delete(f"payments_{self.request.user.id}")  # invalidate cache

    def list(self, request, *args, **kwargs):
        cache_key = f"payments_{request.user.id}"

        data = cache.get(cache_key)

        if not data:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

            cache.set(cache_key, data, timeout=300)

        return Response(data)
        
    def retrieve(self, request, *args, **kwargs):
        payment_id = kwargs.get("pk")
        cache_key = f"payment_{request.user.id}_{payment_id}"

        data = cache.get(cache_key)

        if not data:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data

            cache.set(cache_key, data, timeout=300)

        return Response(data)'''