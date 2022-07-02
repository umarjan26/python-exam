from django.urls import path
from webapp.views import index, create_guest, updates

urlpatterns = [
    path('', index, name="index"),
    path('add/', create_guest, name="add"),
    path('updates/<int:pk>/update', updates, name="updates")

]