from rest_framework import viewsets
from livros.API import serializer
from livros import models
class livrosViewsSets(viewsets.ModelViewSet):
    serializer_class = serializer.livrosSerializers
    queryset = models.livros.objects.all()
