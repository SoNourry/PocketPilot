from enum import Enum
from django.db import models
from .category import Category
from django.conf import settings

FREQUENCY_CHOICES = (
    ("DAILY", "Quotidienne"),
    ("WEEKLY", "Hebdomadaire"),
    ("MONTHLY", "Mensuelle"),
    ("YEARLY", "Annuelle"),
)


class RecurringExpense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(
        max_length=50,
        choices=FREQUENCY_CHOICES,
        default="MONTHLY",
    )
    next_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.montant} due on {self.prochaine_date}"
