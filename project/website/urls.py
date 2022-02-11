from django.urls import path
from . import views

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
]