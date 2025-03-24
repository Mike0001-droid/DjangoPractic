from rest_framework import serializers
from .models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор породы собак. Преобразует queryset в json

    Returns:
        json: Сериализованный json
    """
    dog_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    """
    Сериализатор собак. Преобразует queryset в json

    Returns:
        json: Сериализованный json
    """
    breed = BreedSerializer(read_only=True)
    avg_age = serializers.FloatField(read_only=True)
    same_breed_count = serializers.IntegerField(read_only=True)
    breed_id = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all(),
        source='breed',
        write_only=True
    )
    class Meta:
        model = Dog
        fields = '__all__'

