from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import TaskSerializer
from .models import Task
from rest_framework.permissions import (IsAuthenticated)

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
