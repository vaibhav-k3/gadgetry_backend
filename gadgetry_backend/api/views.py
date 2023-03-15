from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


from .models import User
from .Serializers import UserSerializer
# Create your views here.

class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()



createuserView = CreateUserView.as_view()