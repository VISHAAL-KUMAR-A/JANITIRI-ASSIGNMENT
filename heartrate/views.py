from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from .models import Users, Patient, HeartRateRecord
from .serializers import UserSerializer, PatientSerializer, HeartRateRecordSerializer

# Create your views here.


@api_view(['POST', 'GET'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(
                serializer.validated_data['password'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Please use POST method to register'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = Users.objects.get(email=email)
        if check_password(password, user.password):
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Users.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class HeartRateRecordViewSet(viewsets.ModelViewSet):
    queryset = HeartRateRecord.objects.all()
    serializer_class = HeartRateRecordSerializer
