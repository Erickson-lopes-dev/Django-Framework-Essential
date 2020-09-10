from django.urls import path
from core.views import index, contato

urlpatterns = [
    path('', index),
    path('contato/', contato),
]
