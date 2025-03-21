from django.db import models


CHOICES_SIZES = (
    ('TN', 'Tiny'),
    ('SL', 'Small'),
    ('MD', 'Medium'),
    ('LG', 'Large'),
)

CHOICES_GENDER = (
    ('FM', 'Female'),
    ('ML', 'Male'),
)

class Breed(models.Model):
    name = models.CharField("Название породы", max_length=50)
    size = models.CharField("Размер собаки", choices=CHOICES_SIZES, max_length=6)
    friendliness = models.IntegerField("Дружелюбие")
    trainability = models.IntegerField("Обучаемость")
    shedding_amount = models.IntegerField()
    exercise_needs = models.IntegerField("Необходимость в физ. нагрузках")

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(friendliness__gte=1) & models.Q(friendliness__lt=5),
                name="A friendliness value is valid between 1 and 5",
            ),
            models.CheckConstraint(
                check=models.Q(trainability__gte=1) & models.Q(trainability__lt=5),
                name="A trainability value is valid between 1 and 5",
            ),
            models.CheckConstraint(
                check=models.Q(shedding_amount__gte=1) & models.Q(shedding_amount__lt=5),
                name="A shedding_amount value is valid between 1 and 5",
            ),
            models.CheckConstraint(
                check=models.Q(exercise_needs__gte=1) & models.Q(exercise_needs__lt=5),
                name="A exercise_needs value is valid between 1 and 5",
            ),
        ]

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField("Имя собаки", max_length=50)
    age = models.IntegerField("Возраст")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField("Пол собаки", choices=CHOICES_GENDER, max_length=6)
    color = models.CharField("Цвет", max_length=50)
    favorite_food = models.CharField("Любимая еда", max_length=255)
    favorite_toy = models.CharField("Любимая игрушка", max_length=255)

    def __str__(self):
        return f"{self.breed} - {self.name}"