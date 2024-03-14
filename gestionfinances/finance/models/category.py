# models/transaction.py
from django.db import models

from enum import Enum


class CategoryName(Enum):
    ALIMENTATION = "Alimentation"
    LOISIRS = "Loisirs"
    TRANSPORT = "Transport"
    LOGEMENT = "Logement"
    SANTE = "Santé"
    EDUCATION = "Éducation"
    DIVERS = "Divers"
    EPARGNE = "Épargne"
    INVESTISSEMENTS = "Investissements"
    ASSURANCES = "Assurances"
    UTILITES = "Utilités"  # Electricity, water, internet
    VETEMENTS = "Vêtements"
    CADEAUX = "Cadeaux"
    VOYAGES = "Voyages"
    REMBOURSEMENT = "Remboursement"
    BEAUTE = "Beauté"
    SPORT = "Sport"
    TECHNOLOGIE = "Technologie"
    RESTAURANTS = "Restaurants"
    ANIMAUX = "Animaux"
    LOYER = "Loyer"


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        choices=[(tag.name, tag.value) for tag in CategoryName],
        unique=True,
    )

    def __str__(self):
        return self.get_name_display()
