from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ROLE_CHOICES = [
        ('USER', 'User'),
        ('PATIENT', 'Patient'),
        ('DOCTOR', 'Doctor'),
        ('NURSE', 'Nurse'),
        ('ADMIN', 'Administrator'),
    ]
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='USER')

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f"{self.name}"


class Patient(models.Model):
    user = models.OneToOneField(
        Users, on_delete=models.CASCADE, related_name='patient_profile')
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    weight = models.FloatField()
    height = models.FloatField()

    class Meta:
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"{self.user.name}"


class HeartRateRecord(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='heart_rate_records')
    heart_rate = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-recorded_at']

    def __str__(self):
        return f"Heart Rate for {self.patient}: {self.heart_rate} bpm"
