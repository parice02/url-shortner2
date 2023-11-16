from django.shortcuts import render

# Create your views here.

from app.forms import URLShortForm
from app.models import URLShort


def index(request):
    context = {"form": "Utilisé un instance du formulaire"}
    return render(request, "index.html", context=context)


# 1. Instancier le formulaire avec les données de request.POST/request.GET
# 2. Vérifier si le formulaire est valide. (Si request.POST/request.GET alors le formulaire n'est pas valide).
# 3. Si Le formulaire valide, retourné un message texte (dans *context*) pour dire le formulaire est valide: "message": "Formulaire valide"
# 4. Si le formulaire n'est pas valide. Retourner le formulaire sans message dans context.
