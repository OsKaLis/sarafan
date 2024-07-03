from django import forms

from .models import Basket

class BasketForm(forms.ModelForm):
    """Форма для изменения количества продуктов."""

    class Meta:
        model = Basket
        fields = ('quantity',)
