import os
from django.conf import settings
from django.shortcuts import render
from django.utils.translation import get_language
from .contex import contex, contex_detail
from .forms import Questions, Order

def home(request):
    print(request.POST)
    lang = get_language()
    data = {
        "form": Questions
    }
    return render(request, 'index.html', data)

def detail(request, name):
    print(request.POST)
    lang = get_language()
    template = f"{name}.html"
    exist = os.path.isfile(settings.BASE_DIR / "templates" / template)
    if exist:
        data = {
            "form": Order
        }
        return render(request, template, data)
    else:
        return render(request, "404.html", status=404)
