from rest_framework import serializers
from movie__app.models import Director, Movie, Review


class ReviewSLZ(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class DirectorSLZ(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name count_movies'.split()

class MovieSLZ(serializers.ModelSerializer):
    reviews = ReviewSLZ(many=True)

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews rating'.split()


class Director2SLZ(serializers.ModelSerializer):
    # movie = MovieSLZ(many=True)
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'movie_count'.split()

    def get_movie_count(self, movie):
        return movie.all().count()




