from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['prenom', 'nom', 'metiers', 'age', 'est_inscrit']
        widgets = {
            'est_inscrit': forms.CheckboxInput(),
        }
