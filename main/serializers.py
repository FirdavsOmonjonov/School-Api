from rest_framework import serializers
from .models import Class, Student, Teacher


class ClassSerializer(serializers.ModelSerializer):
    """Serializer for Class."""
    class Meta:
        model = Class
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student."""
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    """Serializer for Teacher."""
    class Meta:
        model = Teacher
        fields = '__all__'

    