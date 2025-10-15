from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin  # ✅ Add login required

from .models import Course
from .forms import CourseForm
from batches.models import Batch
from django.views import View


class CourseListView(LoginRequiredMixin, ListView):
    login_url = '/login/'  # Redirect to login if not authenticated
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"
    ordering = ["-Course_name"]


class CourseDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"


class CourseCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"

    def get_initial(self):
        initial = super().get_initial()
        # Auto-fill Center_id from logged-in user
        if hasattr(self.request.user, "center_id"):
            initial['Center_id'] = self.request.user.center_id
        return initial

    def form_valid(self, form):
        # Ensure Center_id is correctly assigned
        if hasattr(self.request.user, "center_id"):
            form.instance.Center_id = self.request.user.center_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("courses:course_list")


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"
    success_url = reverse_lazy("courses:course_list")

    def form_valid(self, form):
        self.object = form.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"message": "Course updated successfully!"}, status=200)
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)
        return super().form_invalid(form)


class CourseBatchesView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = "batches/batch_list.html"

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        batches = Batch.objects.filter(Course_id=course.id).order_by('-Fiscal_year')
        return render(request, self.template_name, {
            "course": course,
            "batches": batches
        })
