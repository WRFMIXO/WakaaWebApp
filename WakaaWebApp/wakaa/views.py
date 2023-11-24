from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Entreprise, CustomUser, Agence
from .serializers import EntrepriseSerializer, CustomUserSerializer,AgenceSerializer
from .permissions import *
# Create your views here.

# Entreprizes views
class EntrepriseListCreateView(generics.ListCreateAPIView):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    permission_classes = [IsSuperAdmin]

class DetailsEntreprise(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer


# Users Views
class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.request.user.is_superuser:
            return [permissions.AllowAny()]
        elif self.request.user.role == 'admin_entreprise':
            return [permissions.IsAuthenticated(), IsAdminEntreprise()]
        return [permissions.IsAuthenticated()]

# Agences Views
class AgenceListCreateView(generics.ListCreateAPIView):
    queryset = Agence.objects.all()
    serializer_class = AgenceSerializer
    permission_classes = [IsSuperAdmin]