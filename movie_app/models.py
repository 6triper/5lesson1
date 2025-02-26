from django.db import models

# Модель для режиссера
class Director(models.Model):
    name = models.CharField(max_length=255)  # Имя режиссера

    def __str__(self):
        return self.name

# Модель для фильма
class Movie(models.Model):
    title = models.CharField(max_length=255)  # Название фильма
    description = models.TextField()  # Описание фильма
    duration = models.IntegerField()  # Продолжительность в минутах
    director = models.ForeignKey(Director, on_delete=models.CASCADE)  # Связь с режиссером

    def __str__(self):
        return self.title

# Модель для отзыва
class Review(models.Model):
    text = models.TextField()  # Текст отзыва
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Связь с фильмом

    def __str__(self):
        return self.text[:50]  # Показать первые 50 символов отзыва


