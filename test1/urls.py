from site import venv
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.a),
    path('a', views.av.as_view()),
    path('b',views.b),
]
