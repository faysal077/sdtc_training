from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view, logout_view
from sdtc_training import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # Root goes to login page
    path('accounts/', include('accounts.urls')),
    path('dashboard/', main_views.dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),

    # other apps
    path('centers/', include('centers.urls')),
    path('courses/', include('courses.urls')),
    path('batches/', include('batches.urls')),
    path('participants/', include('participants.urls')),
    path('instructors/', include('instructors.urls')),
    path('inventory/', include('inventory.urls')),
    path('budget/', include('budget.urls')),
    path('personnel/', include('personnel.urls')),
]
