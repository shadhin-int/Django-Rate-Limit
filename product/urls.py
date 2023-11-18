from django.urls import path

from product.views import CreateProductView, GetProductsView, DeleteProductView

urlpatterns = [
    path("create", CreateProductView.as_view()),
    path("get", GetProductsView.as_view()),
    path("delete", DeleteProductView.as_view())

]