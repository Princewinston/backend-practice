from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    search_fields = [
        "username","email"
    ]
    filterset_fields = ["username","email"]

    def get_permissions(self):
        if self.action=="create":
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False,methods=["GET"])
    def me(self,request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

