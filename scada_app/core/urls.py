from django.urls import path, include
from django.contrib.auth.decorators import (login_required,
                                            permission_required)
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),  # index page for scada
]
