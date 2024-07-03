from rest_framework import serializers

from products.models import (
    Products, UnderCategory, SizeImage, Category, Basket
)


class BasketUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для изменения количества в корзине."""

    class Meta:
        model = Basket
        fields = ('id', 'quantity', )


class BasketCreateDestroySerializer(serializers.ModelSerializer):
    """Сериализатор для Создания, Удаления корзины."""

    class Meta:
        model = Basket
        fields = ('products', 'quantity', )


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категорий."""
    under_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('name', 'under_category', )

    def get_under_category(self, obj):
        under_categorys = UnderCategory.objects.values('name').filter(category=obj.id)
        return [under_category['name'] for under_category in under_categorys]


class ProductsSerializer(serializers.ModelSerializer):
    """Сериализатор продуктов."""
    current_under_category = serializers.StringRelatedField(read_only=True)
    logo_products = serializers.SerializerMethodField()
    category = serializers.ReadOnlyField(source='current_under_category.category.name')

    class Meta:
        model = Products
        fields = (
            'id',
            'name',
            'slug',
            'category',
            'current_under_category',
            'price',
            'logo_products',
        )

    def get_logo_products(self, obj):
        logo_products = SizeImage.objects.values(
            'size_1', 'size_2', 'size_3'
        ).filter(logo_products=obj.id)
        return list(logo_products[0].values())
