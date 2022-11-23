from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from .models import UserNet
from .serializer import UserSerializer
from .permissions import IsOwnerOrReadOnly



class UserAPIList(generics.ListCreateAPIView):
    queryset = UserNet.objects.all() 
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserNet.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class UserAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserNet.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly)





