from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie__app.serializers import DirectorSLZ, MovieSLZ, ReviewSLZ
from movie__app.models import Director, Movie, Review
@api_view(['GET'])
def directors(request):
    namesDirectors = {
        'name1': 'Oleg',
        'name2': 'Adilet',
        'name3': 'Petr',
    }
    return Response(data=namesDirectors)

@api_view(['GET'])
def DirectorsListView(request):
    directors = Director.objects.all()
    data = DirectorSLZ(directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def MovieListView(request):
    movies = Movie.objects.all()
    data =  MovieSLZ(movies, many=True).data
    return Response(data=data)

@api_view(['GET'])
def ReviewListView(request):
    Reviews = Review.objects.all()
    data = ReviewSLZ(Reviews, many=True).data
    return Response(data=data)

@api_view(['GET'])
def DirectorDetail(request, id):
    DTDirector = Director.objects.get(id=id)
    data = DirectorSLZ(DTDirector).data
    return Response(data=data)

@api_view(['GET'])
def MovieDetail(request, id):
    DTMovie = Movie.objects.get(id=id)
    data = MovieSLZ(DTMovie).data
    return Response(data=data)


@api_view(['GET'])
def ReviewDetail(request, id):
    DTReview = Review.objects.get(id=id)
    data = ReviewSLZ(DTReview).data
    return Response(data=data)