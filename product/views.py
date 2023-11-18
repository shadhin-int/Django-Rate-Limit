from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView

from product.models import Product
from product.serializers import ProductSerializer


class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class GetProductsView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class DeleteProductView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
