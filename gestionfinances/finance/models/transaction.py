from enum import Enum
from django.db import models
from .category import Category
from django.conf import settings


class TransactionType(Enum):
    DEPENSE = "Dépense"
    REVENU = "Revenu"


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    type = models.CharField(
        max_length=7,
        choices=[(tag.name, tag.value) for tag in TransactionType],
        default=TransactionType.DEPENSE.name,
    )

    def __str__(self):
        return f"{self.description} - {self.amount}"
