from site import venv
from django.urls import path
from . import views

urlpatterns = [
    path('', views.a),
    path('b',views.b),
]
