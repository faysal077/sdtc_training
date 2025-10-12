from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Participant, JobHistory
from .forms import ParticipantForm, JobHistoryForm


class ParticipantListView(ListView):
    model = Participant
    template_name = "participants/participant_list.html"
    context_object_name = "participants"
    ordering = ["-id"]


class ParticipantDetailView(DetailView):
    model = Participant
    template_name = "participants/participant_detail.html"
    context_object_name = "participant"


class ParticipantCreateView(CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name = "participants/participant_form.html"
    success_url = reverse_lazy("participant_list")


class ParticipantUpdateView(UpdateView):
    model = Participant
    form_class = ParticipantForm
    template_name = "participants/participant_form.html"
    success_url = reverse_lazy("participant_list")


class JobHistoryCreateView(CreateView):
    model = JobHistory
    form_class = JobHistoryForm
    template_name = "participants/job_history_form.html"

    def form_valid(self, form):
        participant = get_object_or_404(Participant, pk=self.kwargs["pk"])
        form.instance.participant = participant
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("participant_detail", kwargs={"pk": self.kwargs["pk"]})


def toggle_employment_status(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    participant.job_status = "Employed" if participant.job_status != "Employed" else "Unemployed"
    participant.save()
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"status": participant.job_status})
    return redirect("participant_detail", pk=pk)
