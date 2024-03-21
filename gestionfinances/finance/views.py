from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Budget
from .forms import SignUpForm, BudgetForm


def home(request):
    # date_today = timezone.localdate()
    # We need to get current budget for current user
    if request.user.is_authenticated:
        budgets = Budget.objects.filter(user=request.user)
    else:
        budgets = None
    return render(request, "home.html", {"budgets": budgets})


@login_required
def profile(request):
    budgets = Budget.objects.filter(user=request.user)

    return render(request, "profile.html", {"budgets": budgets})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


@login_required
def add_budget(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect("home")
    else:
        form = BudgetForm()

    return render(request, "add_budget.html", {"form": form})
