from rest_framework import serializers
from livros import models

class livrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.livros
        fields = '__all__'
