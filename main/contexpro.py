from django.utils.translation import get_language
from . contex import contex, contex_detail

def contex_text(request):

    data = {
        "contex": contex.get(get_language())
    }
    return data


def contex_text_detail(request):
    data = {
        "contex_detail": contex_detail.get(get_language())
    }

    return data