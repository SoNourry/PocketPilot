from enum import Enum
from django.db import models
from django.conf import settings


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


class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=50,
        choices=[(tag.name, tag.value) for tag in CategoryName],
        unique=True,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # These fields define the validity period of the budget.
    # They enable users to create budgets for specific periods,
    # such as months or fiscal years.
    start_date = models.DateField()
    end_date = models.DateField()

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return (
            f"{self.category} - {self.amount} from {self.start_date} to {self.end_date}"
        )
