from string import ascii_letters
import random

from django.shortcuts import render, redirect

import requests


# Create your views here.

from app.forms import URLShortForm
from app.models import URLShort


def index(request):
    form = URLShortForm(data=request.POST or None)
    context = {"form": form}

    if form.is_valid():
        long_url = form.cleaned_data["long_url"]
        response = requests.get(long_url)
        rand_letters = ""
        if response.ok:
            url_short = form.save()
            while True:
                rand_letters = "".join(random.choices(ascii_letters, k=8))
                s = URLShort.objects.filter(short_url=rand_letters)
                if s.count() == 0:
                    break

            short_url = rand_letters
            url_short.short_url = short_url

            url_short.save()

            context["short_url"] = "http://localhost:8000/" + rand_letters

        else:
            short_url = response.reason
            context["reason"] = response.reason

    return render(request, "index.html", context=context)


def home(request, short=""):
    if short != "":
        url_short = URLShort.objects.filter(short_url=short)
        print(url_short.query)
        url_short = url_short.first()
        if url_short:
            url_long = url_short.long_url
            return redirect(url_long)
    return redirect("/index")
