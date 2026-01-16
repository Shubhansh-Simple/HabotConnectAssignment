# rest_framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# 3rd party
from django_filters.rest_framework import DjangoFilterBackend

# local
from ..models import Employee
from .serializers import EmployeeSerializer


class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department']


class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
