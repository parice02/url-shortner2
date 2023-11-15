from django.shortcuts import render

# Create your views here.


def index(request):
    name = request.GET.get("name")
    prenom = request.GET.get("prenom")
    context = {"variable": "Ceci est une variable", "name": name, "prenom": prenom}
    return render(request, "index.html", context=context)
