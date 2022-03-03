from rest_framework import serializers
from movie__app.models import Director, Movie, Review
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


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

class DirectorСreqteUpdateSrializer(serializers.Serializer):
    name = serializers.CharField()

class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.TimeField()
    director = serializers.IntegerField()

class ReviewCreateUpdateSerialiser(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.CharField()
    stars = serializers.IntegerField(default=5)

class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValueError('такой пользователь уже сущ.')
        return username

class AuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



