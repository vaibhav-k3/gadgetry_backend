from rest_framework.generics import CreateAPIView , ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response


from .models import User
from .Serializers import UserSerializer
# Create your views here.

class ListCreateUserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# class GetAllUsersView(ListAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


class GetUserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

createOrListuserView = ListCreateUserView.as_view()
# getallusers = GetAllUsersView.as_view()
getUser = GetUserDetailView.as_view()