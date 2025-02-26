from django.urls import path
from .views import home, UserCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('', home, name='home'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('me/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]