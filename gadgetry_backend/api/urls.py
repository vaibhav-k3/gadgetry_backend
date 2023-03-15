from django.urls import path

from .views import createuserView ,getallusers, getUser
urlpatterns = [
    path('createUser',createuserView),
    path('getAllUsers',getallusers),
    path('getUser/<str:pk>',getUser)
]