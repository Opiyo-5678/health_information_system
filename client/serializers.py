from rest_framework import serializers
from .models import Client, HealthProgram, Enrollment


class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id', 'name', 'description']


class EnrollmentSerializer(serializers.ModelSerializer):
    program = HealthProgramSerializer()
    
    class Meta:
        model = Enrollment
        fields = ['program', 'enrollment_date', 'notes']


class ClientSerializer(serializers.ModelSerializer):
    programs = serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'full_name', 'date_of_birth', 
                'gender', 'contact_number', 'address', 'programs']
    
    def get_programs(self, obj):
        enrollments = Enrollment.objects.filter(client=obj).select_related('program')
        return EnrollmentSerializer(enrollments, many=True).data