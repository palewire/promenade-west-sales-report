from django.contrib import admin
from django.urls import path
from report import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('admin/', admin.site.urls),
]
