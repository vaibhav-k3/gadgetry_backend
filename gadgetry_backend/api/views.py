from rest_framework.generics import CreateAPIView , ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from .models import User
from .Serializers import UserSerializer
# Create your views here.

class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class GetAllUsersView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class GetUserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

createuserView = CreateUserView.as_view()
getallusers = GetAllUsersView.as_view()
getUser = GetUserDetailView.as_view()