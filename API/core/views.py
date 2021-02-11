from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializer import DadosSerializer
from .models import Dados




class DadosViewSet(viewsets.ModelViewSet):

    queryset = Dados.objects.all()
    serializer_class = DadosSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    
# Create your views here.
