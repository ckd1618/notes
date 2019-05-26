from rest_framework import serializers

from . import models

class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Note
    fields = '__all__'

#this converts our Note model into json data
