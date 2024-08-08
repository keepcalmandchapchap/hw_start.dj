from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sorting = request.GET.get('sort')
    if sorting == 'name':
        sorted_phones = sorted(phones, key=lambda x: x.name)
    elif sorting == 'min_price':
        sorted_phones = sorted(phones, key=lambda x: x.price)
    elif sorting == 'max_price':
        sorted_phones = sorted(phones, key=lambda x: x.price, reverse=True)
    else:
        sorted_phones = phones
    template = 'catalog.html'
    context = {'phones': sorted_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
