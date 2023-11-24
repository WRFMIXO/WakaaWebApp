 # urls.py

from django.urls import path
from .views import EntrepriseListCreateView, DetailsEntreprise, CustomUserListCreateView, AgenceListCreateView

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('entreprises/', EntrepriseListCreateView.as_view(), name='entreprises-list-create'),
    path('agences/', AgenceListCreateView.as_view(), name='agence-list-create'),

    # Entreprises Details
    path('entreprises/<int:pk>/', DetailsEntreprise.as_view(), name='details_entreprise'),
]