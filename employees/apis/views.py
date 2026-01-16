# rest_framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# local
from ..models import Employee
from .serializers import EmployeeSerializer


class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
