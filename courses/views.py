from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Course
from .forms import CourseForm
from django.http import JsonResponse


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"
    ordering = ["-Course_name"]


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"
    success_url = reverse_lazy("courses:course_list")

    def form_valid(self, form):
        self.object = form.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"message": "Course created successfully!"}, status=200)
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)
        return super().form_invalid(form)


class CourseUpdateView(UpdateView):
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


# Placeholder for showing batches under a course
from django.views import View
from django.shortcuts import render


class CourseBatchesView(View):
    template_name = "courses/course_batches.html"

    def get(self, request, pk):
        # You can later replace this with actual Batch model query
        course = Course.objects.get(pk=pk)
        batches = []  # Replace with actual related batches
        return render(request, self.template_name, {"course": course, "batches": batches})
