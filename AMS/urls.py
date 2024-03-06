from django.contrib import admin
from django.urls import path, include
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="ams_home"),
    path('accounts/', include('accounts.urls')),
    path('appointment/', include('appointment.urls')),
]
