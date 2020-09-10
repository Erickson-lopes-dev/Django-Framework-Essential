from django.urls import path
from django.conf.urls import handler404, handler500
from . import views
from .views import index, contato, produto

urlpatterns = [
    path('', index),
    path('contato/', contato),
    path('produto/<int:id>/', produto, name='produto'),
]

handler404 = views.error404
handler500 = views.error500
