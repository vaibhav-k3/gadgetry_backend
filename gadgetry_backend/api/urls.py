from django.urls import path

from .views import getUser,createOrListuserView
urlpatterns = [
    path('ListCreateUser',createOrListuserView),
    path('getUser/<str:pk>',getUser)
]