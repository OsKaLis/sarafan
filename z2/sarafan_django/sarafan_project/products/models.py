from django.db import models

from users.models import Users
from .configurations import (
    DIMENSION_FIELD, SLUG_IDENTIFIER_SIZE,
    DEFAULT_INTERAGER_FIELD,
)


class AbstractionCategories(models.Model):
    """Абстракт для Категирия и ПодКатегирии."""
    name = models.CharField(
        'Название',
        max_length=DIMENSION_FIELD,
    )
    slug = models.SlugField(
        'Индификатор',
        unique=True,
        max_length=SLUG_IDENTIFIER_SIZE,
        null=True
    )
    picture = models.ImageField(
        'Картинка',
        upload_to='recipes/picture/',
        null=True,
        default=None
    )

    class Meta:
        abstract = True


class Category(AbstractionCategories):
    """Таблица Категорий."""
    CATEGORY_TEMPLATE = '{}: {}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.CATEGORY_TEMPLATE.format(
            self.name,
            self.slug,
        )


class UnderCategory(AbstractionCategories):
    """Таблица Под Категорий."""
    UNDER_CATEGORY_TEMPLATE = '{}: {}'
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='сategory',
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.UNDER_CATEGORY_TEMPLATE.format(
            self.name,
            self.slug,
        )


class Products(models.Model):
    """Таблица продуктов."""
    PRODUCTS_TEMPLATE = '{}: {}'
    name = models.CharField(
        'Название',
        max_length=DIMENSION_FIELD,
    )
    slug = models.SlugField(
        'Индификатор',
        unique=True,
        max_length=SLUG_IDENTIFIER_SIZE,
    )
    price = models.PositiveIntegerField(
        'Цена',
        default=DEFAULT_INTERAGER_FIELD
    )
    current_under_category = models.ForeignKey(
        UnderCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='current_under_category',
        verbose_name='Подкатегория'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.PRODUCTS_TEMPLATE.format(
            self.name,
            self.slug,
        )


class Basket(models.Model):
    """Корзина пользователя."""
    user = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True,
        related_name='basket_user',
        verbose_name='Покупатель'
    )
    products = models.ForeignKey(
        Products,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        verbose_name='Продукт'
    )
    quantity = models.PositiveIntegerField(
        'Количество',
        default=DEFAULT_INTERAGER_FIELD
    )

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'


class SizeImage(models.Model):
    """Три варианта картинок для продукта."""
    logo_products = models.OneToOneField(
        Products,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='logo_products',
        verbose_name='Логотип продукта'
    )
    size_1 = models.ImageField(
        'Размер-1',
        upload_to='recipes/size_1/',
        null=True,
        blank=True,
        default=None
    )
    size_2 = models.ImageField(
        'Размер-2',
        upload_to='recipes/size_2/',
        null=True,
        blank=True,
        default=None
    )
    size_3 = models.ImageField(
        'Размер-3',
        upload_to='recipes/size_3/',
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        verbose_name = 'Изображения продукта'
        verbose_name_plural = 'Все изображения продуктов'
