from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Employee
from home.api.serializers import EmployeeSerializer


@api_view(["GET"])
def employee_list_api_view(request):
    """
    :param request:
    :return:
    """
    try:
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response({"There is no Employee post exits in database"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def add_employee_api_view(request):
    """
    :param request:
    :return:
    """
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def update_employee_api_view(request, id):
    """
    :param request:
    :return:
    """
    queryset = Employee.objects.get(pk=id)
    serializer = EmployeeSerializer(queryset, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

