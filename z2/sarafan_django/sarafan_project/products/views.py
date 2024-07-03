from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from users.models import Users
from .forms import BasketForm
from .models import (
    Category, UnderCategory, Products, SizeImage,
    Basket,
)
from sarafan_project.settings import (
    PAGINATION_SIZE,
)


def basket_clean(request):
    """Очистить содержимое своейкорзины."""
    # !!! Задать пользователя корзины
    user = 1
    Basket.objects.filter(user=user).delete()
    return HttpResponseRedirect("/basket/")


def basket(request):
    """Вывод корзину с подсчётом."""
    template = 'basket/basket.html'
    # !!! Задать пользователя корзины
    basket_user = Basket.objects.values(
        'pk', 'products__name', 'quantity',
    )
    product_amount_quantity = Basket.objects.values(
        'products__price', 'quantity',
    )
    results: dict = {'amount': 0, 'quantity': 0}
    sequence_number = 1
    for obj in basket_user:
        obj['sequence_number'] = sequence_number
        sequence_number += 1
    for obj in product_amount_quantity:
        results['amount'] += obj['products__price']*obj['quantity']
        results['quantity'] += obj['quantity']
    context = {'basket_user': basket_user, 'results': results}
    return render(request, template, context)


def basket_del(request, id):
    """Убрать из корзины."""
    basket_id = get_object_or_404(Basket, pk=id)
    basket_id.delete()
    return HttpResponseRedirect("/basket/")


def basket_change_quantity(request, id):
    """Изменить количество продукта в корзине."""
    template = 'basket/basket_change_quantity.html'
    instance = get_object_or_404(Basket, pk=id)
    form = BasketForm(request.POST or None, instance=instance)
    context = {'form': form, 'instance': instance}
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/basket/")
    return render(request, template, context)


def basket_add(request, id):
    """Добавить в корзину."""
    #  Проверка на пользователя
    user = get_object_or_404(Users, pk=1)
    # проверка на наличие продукта
    product = get_object_or_404(Products, pk=id)
    Basket.objects.create(user=user, products=product)
    return HttpResponseRedirect("/all/products/")


def all_products(request):
    """Выгруска всех продуктов."""
    template = 'products/all_products.html'
    products_all = Products.objects.values(
        'name', 'slug', 'current_under_category__category__name',
        'current_under_category__name', 'price', 'pk'
    )
    size_all = SizeImage.objects.values(
        'logo_products', 'size_1', 'size_2', 'size_3'
    )
    paginator = Paginator(products_all, PAGINATION_SIZE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'size_all': size_all}
    return render(request, template, context)


def all_categories(request):
    """Выгруска всех имеющихся катологов и подкатологов."""
    template = 'products/all_categories.html'
    categories_all = Category.objects.values('name')
    Under_categories_all = UnderCategory.objects.values(
        'name', 'category__name'
    )
    paginator = Paginator(categories_all, PAGINATION_SIZE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'Under_categories_all': Under_categories_all,
    }
    return render(request, template, context)
