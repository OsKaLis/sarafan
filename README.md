<div id="header" align="center">
  <h1>Сарафан</h1>
</div>

> [!NOTE]
> ##	Проект магазина продуктов со следующим функционалом:
*	Должна быть реализована возможность создания, редактирования, удаления категорий и подкатегорий товаров в админке.
*	Категории и подкатегории обязательно должны иметь наименование, slug-имя, изображение
*	Подкатегории должны быть связаны с родительской категорией
*	Должен быть реализован эндпоинт для просмотра всех категорий с подкатегориями. Должны быть предусмотрена пагинация.
*	Должна быть реализована возможность добавления, изменения, удаления продуктов в админке.
*	Продукты должны относится к определенной подкатегории и, соответственно категории, должны иметь наименование, slug-имя, изображение в 3-х размерах, цену
*	Должен быть реализован эндпоинт вывода продуктов с пагинацией. Каждый продукт в выводе должен иметь поля: наименование, slug, категория, подкатегория, цена, список изображений
*	Реализовать эндпоинт добавления, изменения (изменение количества), удаления продукта в корзине.
*	Реализовать эндпоинт вывода состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.
*	Реализовать возможность полной очистки корзины
*	Операции по эндпоинтам категорий и продуктов может осуществлять любой пользователь
*	Операции по эндпоинтам корзины может осуществлять только авторизированный пользователь и только со своей корзиной
*	Реализовать авторизацию по токену

### Cтек технологий:
<img src="https://img.shields.io/badge/Python_-3.12-green"> <img src="https://img.shields.io/badge/Django_-3.2.16-green"> <img src="https://img.shields.io/badge/djoser_-2.1.0-black">
<img src="https://img.shields.io/badge/djangorestframework_-3.12.4-black"> <img src="https://img.shields.io/badge/djangorestframework_-4.7.2-black">
<img src="https://img.shields.io/badge/django_bootstrap5_-22.2-black">

### Запуск
* [0] (Клонируем проект):git clone git@github.com:OsKaLis/sarafan.git
* [1] cd z2\sarafan_django
* [2] (Создание файла с настройками ".env"):
>   ```
>   SECRET_KEY=[{Своё значение key}]
>   DEBUG=True
>   ```
* [3] (Запускаем виртуальное окружение):poetry shell
* [4] (Устанавливаем установка зависимости для окружения):poetry install
* [5] (перейти в каталог): cd sarafan_project
* [6] (Применить структуру): python manage.py migrate
* [7] (Создание супер пользователя[windows]): winpty python manage.py createsuperuser
*   ```
    login: admiral
    mail: admiral@mail.ru
    pass:  YVa#ynX#Vz5
    ```
* [8] (Запуск приложение): python manage.py runserver

### Некоторые примеры запросов


### Автор: Юшко Ю.Ю.
