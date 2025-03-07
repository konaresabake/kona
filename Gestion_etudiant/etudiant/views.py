from django.shortcuts import render, get_object_or_404 , redirect

from .models import Etudiant

from .forms import EtudiantForm


def etudiants(request):

    etudiants = Etudiant.objects.all().order_by('-created_at')

    return render(request, 'etudiant/etudiants.html', {'etudiants': etudiants})

# Create your views here.

def details_etudiant(request,id):
    etudiants = get_object_or_404(Etudiant,id = id)
    print(etudiants)

    return render(request, 'etudiant/etudiants_detail.html', {'details_etudiant': details_etudiant})



def index(request):

    return render(request, 'etudiant/index.html', {'index': index})



def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etudiants') 
    else:
        form = EtudiantForm()

    return render(request, 'etudiant/ajouter_etudiant.html', {'form': form})


def modifier_etudiant(request, id):
    etudiant = Etudiant.objects.get(id=id)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiants')  # Rediriger vers la liste des étudiants
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'etudiants/modifier_etudiant.html', {'form': form})



def supprimer_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    etudiant.delete()
    return redirect('etudiants')  # Rediriger vers la liste des étudiants


