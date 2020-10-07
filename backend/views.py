from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from backend.models import Category, Shop
from backend.serializers import CategorySerializer, ShopSerializer


class CategoryView(ListAPIView):
    """
    Класс для просмотра категорий
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ShopView(ListAPIView):
    """
    Класс для просмотра списка магазинов
    """
    queryset = Shop.objects.filter(state=True)
    serializer_class = ShopSerializer