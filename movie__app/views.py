from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie__app.serializers import DirectorSLZ, MovieSLZ, ReviewSLZ, MovieCreateUpdateSerializer, ReviewCreateUpdateSerialiser, DirectorСreqteUpdateSrializer
from movie__app.models import Director, Movie, Review
from rest_framework import status
@api_view(['GET'])
def directors(request):
    namesDirectors = {
        'name1': 'Oleg',
        'name2': 'Adilet',
        'name3': 'Petr',
    }
    return Response(data=namesDirectors)

@api_view(['GET', 'POST'])
def DirectorsListView(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSLZ(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers = DirectorСreqteUpdateSrializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = request.data.get('name')
        Director.objects.create(name=name)
        return Response(data={'message': 'Date Reseived!'})


@api_view(['GET', 'POST'])
def MovieListView(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data =  MovieSLZ(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers =MovieCreateUpdateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors':serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        Movie.objects.create(title=title, description=description, duration=duration,director=director)
        return Response(data={'message': 'Date Reseived!'})

@api_view(['GET', 'POST'])
def ReviewListView(request):
    if request.method == 'GET':
        Reviews = Review.objects.all()
        data = ReviewSLZ(Reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers = ReviewCreateUpdateSerialiser(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        Review.objects.create(text=text,movie=movie,stars=stars)
        return Response(data={'message': 'Date Reseived!'})

@api_view(['GET', 'PUT', 'DELETE'])
def DirectorDetail(request, id):
    try:
        DTDirector = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data='DirectorNotFound')
    if request.method == 'GET':
        data = DirectorSLZ(DTDirector).data
        return Response(data=data)
    elif request.method == 'DELETE':
        DTDirector.delete()
        return Response('no content')
    elif request.method == 'PUT':
        serializers = DirectorСreqteUpdateSrializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        DTDirector.name = request.data.get('name')
        DTDirector.save()
        return Response(data=DirectorSLZ(DTDirector).data)


@api_view(['GET', 'PUT', 'DELETE'])
def MovieDetail(request, id):
    try:
        DTMovie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data='MovieNotFound')
    if request.method == 'GET':
        data = MovieSLZ(DTMovie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        DTMovie.delete()
        return Response('no content')
    elif request.method == 'PUT':
        serializers = MovieCreateUpdateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        DTMovie.name = request.data.get('name')
        DTMovie.save()
        return Response(data=DirectorSLZ(DTMovie).data)



@api_view(['GET'])
def ReviewDetail(request, id):
    try:
        DTReview = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data='ReviewNotFound')
    if request.method == 'GET':
        data = ReviewSLZ(DTReview).data
        return Response(data=data)
    elif request.method == 'DELETE':
        DTReview.delete()
        return Response('no content')
    elif request.method == 'PUT':
        serializers = ReviewCreateUpdateSerialiser(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        DTReview.name = request.data.get('name')
        DTReview.save()
        return Response(data=DirectorSLZ(DTReview).data)

# @api_view(['GET'])
# def listmiviewsbyreviews(request):
#     qeuryset = Movie.objects.all()
#     data = MovieSLZ(qeuryset).data
#     return Response(data=data)

@api_view(['GET'])
def cinema_list_view(request):
        movies = Movie.objects.all()
        serializer = MovieSLZ(movies, many=True)
        return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def directors_list_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSLZ(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers = DirectorСreqteUpdateSrializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        print(request.data)
        name = request.data.get('name')
        Director.objects.create(name=name)
        return Response(data={'message': 'Date Reseived!'})