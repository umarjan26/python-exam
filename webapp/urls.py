from django.urls import path
from webapp.views import index, create_guest

urlpatterns = [
    path('', index, name="index"),
    path('add/', create_guest, name="add")
    # path('article/<int:pk>/', index_view, name="index_view")
]