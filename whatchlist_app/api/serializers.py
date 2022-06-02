from wsgiref.validate import validator
from django.forms import ValidationError
from rest_framework import serializers
from whatchlist_app.models import Movie

def check_name(value):
    if value == 'Jay':
        raise ValidationError('Not Jay')
    return value

class MovieSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[check_name])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self,validated_data):
        return Movie.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance

    def validate_name(self, value):
        if len(value) <= 1:
            raise serializers.ValidationError("Name lenght should be gt 1")
        return value

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Des should be different...")
        return data