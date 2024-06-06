from django.shortcuts import render
from rest_framework import viewsets
from .models import Class, Student, Teacher
from rest_framework import permissions
from .serializers import ClassSerializer, TeacherSerializer, StudentSerializer
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class ClassView(viewsets.ModelViewSet):
    """View set for Class."""
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class TeacherView(viewsets.ModelViewSet):
    """View set for Teacher."""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class StudentView(viewsets.ModelViewSet):
    """View set for Student."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]