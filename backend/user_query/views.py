from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import UserQuery
from .serializers import UserQuerySerializer


class CustomPagination(PageNumberPagination):
    page_size = 100


class UserDataListCreateView(generics.ListCreateAPIView):
    queryset = UserQuery.objects.all()
    serializer_class = UserQuerySerializer
    pagination_class = CustomPagination


class UserDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserQuery.objects.all()
    serializer_class = UserQuerySerializer
