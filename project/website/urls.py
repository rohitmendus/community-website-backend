from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/change_info/<int:id>', views.change_info, name="change_info"),
    path('dashboard/change_urls/<int:id>', views.change_urls, name="change_urls")
]