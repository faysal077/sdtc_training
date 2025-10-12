from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path('add/', views.CourseCreateView.as_view(), name='course_add'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    # batches under a course
    path('<int:pk>/batches/', views.CourseBatchesView.as_view(), name='course_batches'),
]
