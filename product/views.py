from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.throttling import UserRateThrottle

from product.models import Product
from product.serializers import ProductSerializer


class CreateProductView(CreateAPIView):
    throttle_scope = "low"
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class GetProductsView(ListAPIView):
    throttle_scope = "high"
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class DeleteProductView(DestroyAPIView):
    throttle_scope = "low"
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
