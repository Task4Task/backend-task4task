from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("chats/<int:user_id>/", views.get_chats_by_user),
    path("chat/chat/<int:chat_id>/", views.get_chat_by_id),
]
