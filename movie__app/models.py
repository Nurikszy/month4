from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=90)

    @property
    def count_movies(self):
        return self.movies.all().count()

    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.TimeField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def rating(self):
        p = 0
        for i in self.reviews.all():
            p += int(i.stars)
        return p/self.reviews.all().count()


class Review(models.Model):
    STARS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
    text = models.TextField(max_length=100)
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(choices=STARS, null=True)


    def __str__(self):
        return self.text