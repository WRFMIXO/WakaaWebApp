# serializers.py

from rest_framework import serializers
from .models import Agence, Bus, CustomUser, Entreprise, Portefeuille, RecherchePlatform, Ticket, Reservation

# Serializer pour les entreprises
class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'

# Serialiser pour les utilisateurs
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

# Serialiser pour les Agences
class AgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agence
        fields = '__all__'