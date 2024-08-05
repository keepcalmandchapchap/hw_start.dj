from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(BUS_STATION_CSV, encoding='utf-8') as f:
        bus_stations_list = [station for station in csv.DictReader(f)]

    paginator = Paginator(bus_stations_list, 25)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'bus_stations': page_obj,
        'page': paginator.page(page_number),
    }
    return render(request, 'stations/index.html', context)
