from django.urls import path

from .views import (
    ProductsList, CategoryList, BasketListCreateUpdateDestroy,
    BasketClean,
)

app_name = 'api'

urlpatterns = [
    # эндпоинт изменения (изменение количества) в корзине.
    # эндпоинт удаления продукта в корзине.
    # эндпоинт добавления в корзине.
    # Эндпоинт вывода состава корзины с подсчетом количества товаров
    # и суммы стоимости товаров в корзине.
    path('basket', BasketListCreateUpdateDestroy.as_view()),

    # эндпоинт реализовать возможность полной очистки корзины
    path('basket/clean', BasketClean.as_view()),

    # Эндпоинт для просмотра всех категорий с подкатегориями.
    path('all/categories/', CategoryList.as_view()),

    # Эндпоинт вывода продуктов с пагинацией.
    path('all/products/', ProductsList.as_view()),
]
