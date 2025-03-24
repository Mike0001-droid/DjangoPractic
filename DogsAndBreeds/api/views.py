from django.db.models import Avg, Count, OuterRef, Subquery
from rest_framework import viewsets
from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """
    Вьюсет породы собак. Реализует базовый CRUD 
    модели Breed
    """
    queryset = Breed.objects.annotate(dog_count=Count('dogs'))
    serializer_class = BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    """
    Вьюсет собак. Реализует базовый CRUD 
    модели Dog
    """
    queryset = Dog.objects.annotate(
        avg_age=Subquery(
            Dog.objects.filter(breed=OuterRef('breed'))
            .values('breed')
            .annotate(avg_age=Avg('age'))
            .values('avg_age')
        ),
        same_breed_count=Count('breed__dogs')
    )
    serializer_class = DogSerializer
