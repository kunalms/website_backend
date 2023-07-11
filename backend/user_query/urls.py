from django.urls import path
from .views import UserDataListCreateView, UserDataRetrieveUpdateDestroyView

urlpatterns = [
    path('userquery/', UserDataListCreateView.as_view(), name='userdata-list-create'),
    path('userquery/<int:pk>/', UserDataRetrieveUpdateDestroyView.as_view(), name='userdata-retrieve-update-destroy'),
]
