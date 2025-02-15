from rest_framework import serializers
from .models import Users, Patient, HeartRateRecord


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}


class PatientSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'user', 'user_name', 'user_email',
                  'age', 'gender', 'weight', 'height']


class HeartRateRecordSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(
        source='patient.user.name', read_only=True)

    class Meta:
        model = HeartRateRecord
        fields = ['id', 'patient', 'patient_name', 'heart_rate', 'recorded_at']
