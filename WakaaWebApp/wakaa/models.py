from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ROLES = [
        ('superadmin', 'Super Administrateur'),
        ('admin_entreprise', 'Admin d\'Entreprise'),
        ('employe_agence', 'Employé d\'Agence'),
        ('client', 'Client'),
    ]

    ROLES_AGENCES = [
        ('gestion_flotte', 'Gestion de la Flotte'),
        ('maintenance_vehicules', 'Maintenance Des Véhicules'),
        # Ajouter d'autres rôles par la suite
    ]

    role = models.CharField(max_length=20, choices=ROLES)
    role_agence = models.CharField(max_length=50, choices=ROLES_AGENCES, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )

class Entreprise(models.Model):
    admin_entreprise = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    data_creation = models.DateField()
    # Ajouter d'autres champs spécifiques selon les besoins

class Agence(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    date_creation = models.DateField()
    # Ajouter d'autres champs spécifiques selon les besoins 

class Portefeuille(models.Model):
    proprietaire = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    solde = models.DecimalField(max_digits=10, decimal_places=4)
    historique_transactions = models.TextField()
    # Ajouter d'autres champs spécifiques selon les besoins

class Ticket(models.Model):
    destination = models.CharField(max_length=255)
    depart = models.CharField(max_length=255)
    date_depart = models.DateTimeField()
    date_arrivee_prevue = models.DateTimeField()
    duree_trajet = models.DurationField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    passager = models.CharField(max_length=255)
    # Ajouter d'autres champs spécifiques selon les besoins

class Reservation(models.Model):
    STATUT_CHOICES = [
        ('attente', 'En Attente'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
    ]

    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reservations_client')
    passager = models.CharField(max_length=255)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    # Ajouter d'autres champs spécifiques selon les besoins

class RecherchePlatform(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mot_cle = models.CharField(max_length=255)
    filtres = models.JSONField()
    date_recherche = models.DateTimeField(auto_now_add=True)
    # Ajouter d'autres champs spécifiques selon les besoins

class Bus(models.Model):
    TYPE_BUS_CHOICES = [
        ('coaster', 'COASTER (30 places assises)'),
        ('cargo', 'CARGO (17 places assises)'),
        ('autobus', 'AUTOBUS (50 places assises)'),
        ('longbus', 'AUTOBUS LONG (70 places assises)'),
    ]

    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    type_bus = models.CharField(max_length=255, choices=TYPE_BUS_CHOICES, blank=False)
    nombre_places = models.PositiveBigIntegerField()
    disposition_seats = models.JSONField()
    # Ajouter d'autres champs spécifiques selon les besoins

