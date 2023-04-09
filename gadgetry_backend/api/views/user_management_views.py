from rest_framework.generics import CreateAPIView , ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


from ..models import User
from ..Serializers import UserSerializer
# Create your views here.

class ListCreateUserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class GetUserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserVerification(APIView):

    def post(self, request):

        userName = request.POST.get('userName')
        userPassword = request.POST.get('userPassword')

        number_of_user = User.objects.filter(userName = userName , userPassword = userPassword).count()

        if number_of_user > 0:
            return Response({
                'status':'User Found'
            })
        else:
            return Response({
                'status':'User not Found'
            })


createOrListuserView = ListCreateUserView.as_view()
# getallusers = GetAllUsersView.as_view()
getUser = GetUserDetailView.as_view()
verifyUser = UserVerification.as_view()