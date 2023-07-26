from django.shortcuts import render
from django.http import HttpResponse
from women.models import Women

#
# def index(request):
#     return render(request, "index.html")
#
#
# def category(request, cats_id):
#     return HttpResponse(f"<h1>Статьи по категориям</h1> {cats_id}")
#
#
# def women_name(request, name):
#     return HttpResponse(f"<p>Женщину зовут {name}</p>")


# CRUD - Create, Retrieve, Update, Delete
# Create - post запрос
# Retrieve - get запрос
# Update - put запрос
# Delete

# def index(request):
#     data = {"header": "Hello Django", "message": "Welcome to python"}
#     return render(request, "index.html", context=data)


# def index(request):
#     header = "Данные пользователя"  # обычная переменная
#     langs = ["Python", "Java", "C#"]  # список
#     user = {"name": "Tom", "age": 23}  # словарь
#     address = ("Абрикосовая", 23, 45)  # кортеж
#
#     data = {"header": header, "langs": langs, "user": user, "address": address}
#     return render(request, "index.html", context=data)


# def about(request):
#     header = "Расскажи о себе"
#     langs = ["English", "Russia", "Spanish", "French", "China"]
#     user = ['Shilamita', 'Sakura', 'Naruto', 'Hurem', 'Hinata', 'Erzhan', 'Aicholpon', "Killua"]
#     address = ("Ottava", "Ankara", "Madrid", "Kanoha", "Rome", "Paris", "Amsterdam")
#
#     data = {"header": header, "langs": langs, "user": user, "address": address}
#     return render(request, "about.html", context=data)
menu = ["О сайте", "Добавить статью", "обратная связь", "Войти"]


def index(request):
    posts = Women.objects.filter(is_published=True)
    data = {"menu": menu, "title": "Главная страница", "posts": posts}
    return render(request, "index.html", data)


def about(request):
    # posts = Women.objects.all()
    data = {"menu": menu, "title": "О сайте"}
    return render(request, "about.html", data)
