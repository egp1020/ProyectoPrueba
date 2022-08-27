from django.urls import path
from .views import familiar

urlpatterns = [
    path('', familiar),
]