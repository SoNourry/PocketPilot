from django.db import models
from .category import Category
from django.conf import settings


class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
