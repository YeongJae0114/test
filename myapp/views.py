from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProductSerializer
from .models import Product

class ProductViewSet(ModelViewSet):
    #어떤 모델을 다룰 것인지 정하는 쿼리셋
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


