from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, 'app_blog/hex_to_dec.html', {})


def single_page(request, *args, **kwargs):
    return render(request, 'app_blog/Single_page.html', {})
