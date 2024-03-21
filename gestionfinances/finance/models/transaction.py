from enum import Enum
from django.db import models
from django.conf import settings
from .budget import Budget


class TransactionType(Enum):
    DEPENSE = "Dépense"
    REVENU = "Revenu"


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    budget = models.ForeignKey(
        Budget,
        on_delete=models.CASCADE,
        related_name="transactions",
        null=True,
        blank=True,
    )
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
