from site import venv
from django.urls import path
from . import views

urlpatterns = [
    path('a', views.a),
    path('', views.av.as_view()),
    path('b',views.b),
]
