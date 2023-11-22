# Generated by Django 4.2.7 on 2023-11-22 13:41

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=15)),
                ('date_creation', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('superadmin', 'Super Administrateur'), ('admin_entreprise', "Admin d'Entreprise"), ('employe_agence', "Employé d'Agence"), ('client', 'Client')], max_length=20)),
                ('role_agence', models.CharField(blank=True, choices=[('gestion_flotte', 'Gestion de la Flotte'), ('maintenance_vehicules', 'Maintenance Des Véhicules')], max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('depart', models.CharField(max_length=255)),
                ('date_depart', models.DateTimeField()),
                ('date_arrivee_prevue', models.DateTimeField()),
                ('duree_trajet', models.DurationField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('passager', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passager', models.CharField(max_length=255)),
                ('date_reservation', models.DateTimeField()),
                ('statut', models.CharField(choices=[('attente', 'En Attente'), ('confirmee', 'Confirmée'), ('annulee', 'Annulée')], max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_client', to='wakaa.customuser')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wakaa.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='RecherchePlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mot_cle', models.CharField(max_length=255)),
                ('filtres', models.JSONField()),
                ('date_recherche', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wakaa.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Portefeuille',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solde', models.DecimalField(decimal_places=4, max_digits=10)),
                ('historique_transactions', models.TextField()),
                ('proprietaire', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wakaa.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=15)),
                ('data_creation', models.DateField()),
                ('admin_entreprise', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wakaa.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_bus', models.CharField(choices=[('coaster', 'COASTER (30 places assises)'), ('cargo', 'CARGO (17 places assises)'), ('autobus', 'AUTOBUS (50 places assises)'), ('longbus', 'AUTOBUS LONG (70 places assises)')], max_length=255)),
                ('nombre_places', models.PositiveBigIntegerField()),
                ('disposition_seats', models.JSONField()),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wakaa.agence')),
                ('entreprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wakaa.entreprise')),
            ],
        ),
        migrations.AddField(
            model_name='agence',
            name='entreprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wakaa.entreprise'),
        ),
    ]