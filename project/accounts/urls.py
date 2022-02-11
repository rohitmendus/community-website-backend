from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.sign_in, name="sign_in"),
    path('sign-in/<str:tab>', views.show_register, name="sign_in_register"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout")
]

