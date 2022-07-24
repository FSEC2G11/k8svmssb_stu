from rest_framework import serializers
from .models import VacDoseStatus, Student

class VacStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacDoseStatus
        fields = ['id', 'sid', 'vacName', 'vacDateD1', 'vacDateD2']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['sid', 'sfname', 'slname', 'dob', 'gidtype', 'gidno', 'mobile', 'email', 'vaccine']


class VacReportSerializer(serializers.ModelSerializer):
    vac_details = VacStatusSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['sid', 'sfname', 'slname', 'dob', 'gidtype', 'gidno', 'mobile', 'email', 'vaccine', 'vac_details' ]

