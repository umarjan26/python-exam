from django.urls import path
from webapp.views import index

urlpatterns = [
    path('', index, name="index")
    # path('add/', create_task, name="add"),
    # path('article/<int:pk>/', index_view, name="index_view")
]