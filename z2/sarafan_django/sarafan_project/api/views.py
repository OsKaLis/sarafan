from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from products.models import (
    UnderCategory, Category, Products, SizeImage, Basket
)
from .serializers import (
    ProductsSerializer, CategorySerializer,
    BasketCreateDestroySerializer, BasketUpdateSerializer
)


class BasketClean(APIView):
    """Полное удаление продуктов из корзины."""

    def delete(self, request):
        id_user = self.request.user.id
        # Добавить в запрос проверку пользователя
        instance = Basket.objects.filter(user=id_user) ## ???(Basket, user=id_user)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BasketListCreateUpdateDestroy(APIView):
    """Показать всю корзину."""

    def get(self, request):
        user = self.request.user
        products = Basket.objects.values(
            'products__name',
            'quantity',
            'products__price'
        ).filter(user=1) ## ??? Настройк юзера
        result = {
            'products': products,
            'amount': 0,
            'quantity': 0,
        }
        for product in products:
            result['amount'] += product['products__price'] * product['quantity']
            result['quantity'] += product['quantity']
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        user = self.request.user
        request.data['user'] = user.pk
        serializer = BasketCreateDestroySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id_product = request.data['id']
        # Добавить в запрос проверку пользователя
        instance = get_object_or_404(Basket, pk=id_product)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request):
        id_product = request.data['id']
        # Добавить в запрос проверку пользователя
        instance = get_object_or_404(Basket, pk=id_product)
        serializer = BasketUpdateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryList(generics.ListAPIView):
    """Просмотра всех категорий с подкатегориями."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsList(generics.ListAPIView):
    """Вывода продуктов."""
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
