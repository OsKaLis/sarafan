from django.contrib import admin

from .models import Users


@admin.register(Users)
class UsersPanel(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
        'user_name',
        'first_name',
        'last_name',
        'password',
    )
    list_editable = ('password',)
    list_filter = ('user_name', 'email')
    search_fields = ('user_name', 'email')
    empty_value_display = '-пусто-'
