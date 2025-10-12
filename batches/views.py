from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Batch
from .forms import BatchForm


class BatchListView(ListView):
    model = Batch
    template_name = "batches/batch_list.html"
    context_object_name = "batches"
    ordering = ["-Fiscal_year"]


class BatchDetailView(DetailView):
    model = Batch
    template_name = "batches/batch_detail.html"
    context_object_name = "batch"


class BatchCreateView(CreateView):
    model = Batch
    form_class = BatchForm
    template_name = "batches/batch_form.html"
    success_url = reverse_lazy("batch_list")


class BatchParticipantsView(View):
    template_name = "batches/batch_participants.html"

    def get(self, request, pk):
        batch = Batch.objects.get(pk=pk)
        participants = []  # Later: fetch related participants from Participant_table
        return render(request, self.template_name, {"batch": batch, "participants": participants})
