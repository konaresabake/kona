from django.urls import path
from .views import *


urlpatterns = [
    path('etud/', liste_etudiants , name='liste_etudiants'),

    path('index/', index , name='index'),

    path('details/<int:id>', details_etudiant , name='details_etudiant'),

    path('ajouter/', ajouter_etudiant , name='ajouter_etudiant'),

    path('modifier/<int:id>/', modifier_etudiant, name='modifier_etudiant'),

    path('supprimer/<int:id>/', supprimer_etudiant, name='supprimer_etudiant'),

]
