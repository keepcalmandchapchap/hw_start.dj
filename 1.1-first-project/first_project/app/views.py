from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    workdir_list = os.listdir(r'C:\Users\user\OneDrive\Рабочий стол\netology\django_hw\dj-homeworks\1.1-first-project\first_project')
    msg = f'Файлы текущей директории:\n \
{', '.join(workdir_list)}'
    return HttpResponse(msg)
    # raise NotImplemented
