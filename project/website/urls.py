from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/change_info/<int:id>', views.change_info, name="change_info"),
    path('dashboard/change_urls/<int:id>', views.change_urls, name="change_urls"),
    path('delete_account/', views.delete_account, name="delete_account"),
    path('add_friend/<int:id>', views.add_friend, name="add_friend"),
    path('profile/<int:id>', views.profile, name="profile"),
    path('accept_friend_request/<int:id>', views.accept_friend_request, name="accept_friend_request"),
    path('decline_friend_request/<int:id>', views.decline_friend_request, name="decline_friend_request"),
    path('change_password/', views.change_password, name="change_password"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_done/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
    path('add_article/', views.add_article, name="add_article"),
    path('add_book_review/', views.add_book_review, name="add_book_review"),
    path('add_image/', views.add_image, name="add_image"),
]