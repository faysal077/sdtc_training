from datetime import datetime

from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from centers.models import Center
from .forms import BatchForm
from django.views.generic import ListView
from courses.models import Course
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from participants.models import Participant
from .models import Batch

class BatchByCourseView(ListView):
    model = Batch
    template_name = "batches/batches_by_course.html"
    context_object_name = "batches"
    ordering = ["-id"]

    def get_queryset(self):
        self.course = get_object_or_404(Course, pk=self.kwargs['course_id'])
        return Batch.objects.filter(Course_id=self.course.id).order_by('-Fiscal_year')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.course
        return context


class BatchListView(ListView):
    model = Batch
    template_name = "batches/batch_list.html"
    context_object_name = "batches"
    ordering = ["-Fiscal_year"]


class BatchDetailView(DetailView):
    model = Batch
    template_name = "batches/batch_detail.html"
    context_object_name = "batch"


@method_decorator(login_required, name='dispatch')
class BatchCreateView(CreateView):
    model = Batch
    form_class = BatchForm
    template_name = "batches/batch_form.html"

    def get_initial(self):
        """Auto-fill Center_id and Course_id in form."""
        initial = super().get_initial()
        course_id = self.request.GET.get("course_id")
        center_id = getattr(self.request.user, "center_id", None)

        if course_id:
            initial["Course_id"] = course_id
        if center_id:
            initial["Center_id"] = center_id
        return initial

    def form_valid(self, form):
        """Auto-assign Center, Course, and Fiscal Year before saving."""
        course_id = self.request.GET.get("course_id")
        center_id = getattr(self.request.user, "center_id", None)

        # Assign related fields automatically
        if course_id:
            form.instance.Course_id = get_object_or_404(Course, id=course_id)
        if center_id:
            form.instance.Center_id = get_object_or_404(Center, id=center_id)

        # --- Auto-calculate Fiscal Year ---
        start_date = form.cleaned_data.get("Actual_start_date")
        end_date = form.cleaned_data.get("Actual_end_date")

        if start_date:
            fiscal_year_start = self.get_fiscal_year_start(start_date)
            fiscal_year_end = fiscal_year_start + 1
            # Store in readable format like "2024–2025"
            form.instance.Fiscal_year = datetime(fiscal_year_start, 7, 1, 0, 0, 0)

        self.object = form.save()

        # --- AJAX success response ---
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "success": True,
                "message": "✅ Batch saved successfully!"
            })

        return super().form_valid(form)

    def get_fiscal_year_start(self, start_date):
        """Return the start year of the fiscal year (July–June)."""
        return start_date.year if start_date.month >= 7 else start_date.year - 1

    def form_invalid(self, form):
        """Handle AJAX form errors."""
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "success": False,
                "errors": form.errors
            })
        return super().form_invalid(form)

    def get_success_url(self):
        """Redirect to batch list by course after save."""
        return reverse("batches:batches_by_course", args=[self.object.Course_id.id])


class BatchParticipantsView(View):
    template_name = "participants/participant_list.html"

    def get(self, request, pk):
        batch = get_object_or_404(Batch, pk=pk)
        participants = Participant.objects.filter(batch_id=batch)
        return render(request, self.template_name, {
            "batch": batch,
            "participants": participants
        })

