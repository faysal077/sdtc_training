from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View

from batches.models import Batch
from .models import Participant, JobHistory
from .forms import ParticipantForm, JobHistoryForm


# --------------------------
# Participant List & Detail
# --------------------------
# views.py
class ParticipantListView(ListView):
    model = Participant
    template_name = "participants/participant_list.html"
    context_object_name = "participants"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batch = get_object_or_404(Batch, pk=self.kwargs['pk'])
        context['batch'] = batch
        return context

    def get_queryset(self):
        batch = get_object_or_404(Batch, pk=self.kwargs['pk'])
        return Participant.objects.filter(batch=batch).order_by("-id")



class ParticipantDetailView(DetailView):
    model = Participant
    template_name = "participants/participant_detail.html"
    context_object_name = "participant"


class ParticipantUpdateView(UpdateView):
    model = Participant
    form_class = ParticipantForm
    template_name = "participants/participant_form.html"
    success_url = reverse_lazy("participants:participant_list")


# --------------------------
# AJAX: Add Participant Modal
# --------------------------
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Participant
from .forms import ParticipantForm
from batches.models import Batch

def participant_add_ajax(request, batch_id):
    batch = get_object_or_404(Batch, id=batch_id)

    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.batch_id = batch
            participant.course_id = batch.Course_id  # ✅ Correct field name
            participant.save()

            participants = Participant.objects.filter(batch_id=batch)
            html = render_to_string("participants/participant_table.html", {"participants": participants})
            return JsonResponse({"success": True, "html": html})
        else:
            form_html = render_to_string("participants/participant_form.html", {"form": form}, request=request)
            return JsonResponse({"success": False, "form_html": form_html})

    else:
        # GET request → return form HTML
        form = ParticipantForm(initial={"batch_id": batch.id, "course_id": batch.Course_id.id})
        return render(request, "participants/participant_form.html", {"form": form})


# --------------------------
# Job History (placeholder)
# --------------------------
class JobHistoryCreateView:
    pass


# --------------------------
# Toggle Employment Status
# --------------------------
def toggle_employment_status(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    participant.job_status = "Employed" if participant.job_status != "Employed" else "Unemployed"
    participant.save()
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"status": participant.job_status})
    return redirect("participants:participant_detail", pk=pk)
