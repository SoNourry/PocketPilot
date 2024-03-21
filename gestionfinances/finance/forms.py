# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.forms as forms
from .models import Transaction
from .models import Budget


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount", "date", "description", "type"]


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ["category", "amount", "start_date", "end_date", "description"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }
