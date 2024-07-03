from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    # эндпоинт добавления в корзине.
    path('basket/<int:id>/add/', views.basket_add, name='basket_add'),

    # эндпоинт изменения (изменение количества) в корзине.
    path(
        'basket/<int:id>/change_quantities/',
        views.basket_change_quantity,
        name='basket_change_quantity'
    ),

    # эндпоинт удаления продукта в корзине.
    path('basket/<int:id>/del/', views.basket_del, name='basket_del'),

    # эндпоинт вывода состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.
    path('basket/', views.basket, name='basket'),

    # эндпоинт реализовать возможность полной очистки корзины
    path('basket/clean/', views.basket_clean, name='basket_clean'),

    # эндпоинт вывода продуктов с пагинацией.
    path('all/products/', views.all_products, name='all_products'),

    # эндпоинт для просмотра всех категорий с подкатегориями. Должны быть предусмотрена пагинация.
    path('all/categories/', views.all_categories, name='all_categories'),
]
