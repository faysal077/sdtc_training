from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Batch
from .forms import BatchForm
from .forms import BatchForm
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from courses.models import Course
from .models import Batch
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Batch
from participants.models import Participant  # ✅ import your Participant model


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


class BatchCreateView(CreateView):
    model = Batch
    form_class = BatchForm
    template_name = "batches/batch_form.html"

    def form_valid(self, form):
        course_id = self.request.GET.get("course_id")
        if course_id:
            form.instance.Course_id_id = course_id
        self.object = form.save()

        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"success": True, "message": "✅ Batch saved successfully!"})
        else:
            return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"success": False, "errors": form.errors})
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        course_id = self.object.Course_id.id
        return reverse("batches:batches_by_course", args=[course_id])


# batches/views.py
from django.shortcuts import render, get_object_or_404
from django.views import View
from participants.models import Participant
from .models import Batch

class BatchParticipantsView(View):
    template_name = "participants/participant_list.html"

    def get(self, request, pk):
        batch = get_object_or_404(Batch, pk=pk)
        participants = Participant.objects.filter(batch_id=batch)
        return render(request, self.template_name, {
            "batch": batch,
            "participants": participants
        })

