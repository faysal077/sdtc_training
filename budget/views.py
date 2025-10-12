from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Budget


# Django ModelForm for Budget
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = [
            "center_id",
            "name",
            "echonomic_code",
            "description",
            "allocation",
            "achivement",
            "requirement",
        ]


def budget_list(request):
    budgets = Budget.objects.all().order_by("-id")
    return render(request, "budget/budget_list.html", {"budgets": budgets})


# budget/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Budget
from .forms import BudgetForm

def add_budget(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Budget added successfully!'})
            return redirect("budget:list")
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = BudgetForm()
    return render(request, "budget/budget_form.html", {"form": form, "title": "Add Budget"})



def edit_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id)
    if request.method == "POST":
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = BudgetForm(instance=budget)
    return render(request, "budget/budget_form.html", {"form": form, "title": "Edit Budget"})


def delete_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id)
    if request.method == "POST":
        budget.delete()
        return redirect("list")
    return render(request, "budget/budget_confirm_delete.html", {"budget": budget})
