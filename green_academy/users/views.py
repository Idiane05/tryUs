from rest_framework import generics, permissions
from users.serializers import UserSerializer, UserCreateSerializer
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()

def home(request):
    return HttpResponse("Welcome to Green Academy App! (Signed by Willie and Philippa)")

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user