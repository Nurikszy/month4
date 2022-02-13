from rest_framework import serializers
from movie__app.models import Director, Movie, Review

class DirectorSLZ(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSLZ(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSLZ(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

