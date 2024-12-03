from django.urls import path
from .import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),
    path('upload', views.upload_image, name='upload_image'),
    path('clear', views.ClearChathistory, name="clear-chat-history")
] 

