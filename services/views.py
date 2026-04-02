from django.shortcuts import render, get_object_or_404
from.forms import TraiteurForm
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Traiteur

def liste_traiteurs(request):
    traiteurs = Traiteur.objects.all()
    context = {
        'traiteurs' : traiteurs
    }
    return render(request, 'liste.html', context)

def detail(request, id):
    traiteur =get_object_or_404(Traiteur, id= id)
    return render(request, 'detail_traiteur.html', {'traiteur':traiteur})


@login_required
def ajouter_traiteur(request):
    success_msg = None
    if request.method == "POST":
        form = TraiteurForm(request.POST)
        if form.is_valid():
            form.save()
            success_msg = "Vous etes enregistres avec succes"
            form = TraiteurForm()

    else:
        form = TraiteurForm()

    context = {
        'form' : form,
        'success_msg': success_msg
    }
    return render(request, 'ajouter_traiteur.html', context)
    
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'