from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from category.models import Category

from .models import Service
from .serializers import ServiceSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_services_by_receiver_id(request, receiver_id):
    services = Service.objects.filter(receiver=receiver_id)
    serializer = ServiceSerializer(services, many=True)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_service_by_id(request, id):
    service = get_object_or_404(Service, id=id)

    serializer = ServiceSerializer(service, many=True)

    serializer = ServiceSerializer(service)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_service(request):
    # Extracting data from request
    title = request.data.get("title")
    description = request.data.get("description")
    receiver = request.data.get("receiver")

    # Validating if required data is present
    if not title or not description:
        return Response(
            {"error": "Title and description are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Creating the service instance with provided data
    service_instance = {
        "title": title,
        "description": description,
        "receiver": receiver,  # Assuming receiver is a foreign key field
    }

    # Creating serializer instance with data and context
    serializer = ServiceSerializer(data=service_instance, context={"request": request})

    # Validating serializer data
    if serializer.is_valid():
        # Saving the serializer instance
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_service(request, service_id):
    print("update_service")
    service = get_object_or_404(Service, id=service_id)
    # I need to change the service.status to false
    service.status = False
    service.save()

    serializer = ServiceSerializer(service)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_service(request):
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        successfullstatus = status.HTTP_201_CREATED
        return Response(serializer.data, successfullstatus)
    else:
        badstatus = status.HTTP_400_BAD_REQUEST
        return Response(serializer.errors, badstatus)
