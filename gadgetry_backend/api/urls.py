from django.urls import path

from .views import createuserView
urlpatterns = [
    path('createUser',createuserView)
]