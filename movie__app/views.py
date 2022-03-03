from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from movie__app.serializers import DirectorSLZ, MovieSLZ, ReviewSLZ, MovieCreateUpdateSerializer, ReviewCreateUpdateSerialiser, DirectorСreqteUpdateSrializer, UserCreateSerializer, AuthorizationSerializer
from movie__app.models import Director, Movie, Review
from rest_framework import status
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.views import APIView
# @api_view(['GET'])
# def directors(request):
#     namesDirectors = {
#         'name1': 'Oleg',
#         'name2': 'Adilet',
#         'name3': 'Petr',
#     }
#     return Response(data=namesDirectors)

# @api_view(['GET', 'POST'])
# def DirectorsListView(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         data = DirectorSLZ(directors, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializers = DirectorСreateUpdateSrializer(data=request.data)
#         if not serializers.is_valid():
#             return Response(data={'errors': serializers.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         name = request.data.get('name')
#         Director.objects.create(name=name)
#         return Response(data={'message': 'Date Reseived!'})

class DirectorListCreateAPIView(ListCreateAPIView, GenericAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSLZ


# @api_view(['GET', 'POST'])
# def MovieListView(request):
#     permissions_classes = [permissions.IsAuthenticated]
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         data =  MovieSLZ(movies, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializers =MovieCreateUpdateSerializer(data=request.data)
#         if not serializers.is_valid():
#             return Response(data={'errors':serializers.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         title = request.data.get('title')
#         description = request.data.get('description')
#         duration = request.data.get('duration')
#         director = request.data.get('director')
#         Movie.objects.create(title=title, description=description, duration=duration,director=director)
#         return Response(data={'message': 'Date Reseived!'})

class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSLZ

# @api_view(['GET', 'POST'])
# def ReviewListView(request):
#     if request.method == 'GET':
#         Reviews = Review.objects.all()
#         data = ReviewSLZ(Reviews, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializers = ReviewCreateUpdateSerialiser(data=request.data)
#         if not serializers.is_valid():
#             return Response(data={'errors': serializers.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         text = request.data.get('text')
#         movie = request.data.get('movie')
#         stars = request.data.get('stars')
#         Review.objects.create(text=text,movie=movie,stars=stars)
#         return Response(data={'message': 'Date Reseived!'})

class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSLZ

# @api_view(['GET', 'PUT', 'DELETE'])
# def DirectorDetail(request, id):
#     try:
#         DTDirector = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data='DirectorNotFound')
#     if request.method == 'GET':
#         data = DirectorSLZ(DTDirector).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         DTDirector.delete()
#         return Response('no content')
#     elif request.method == 'PUT':
#         serializers = DirectorСreqteUpdateSrializer(data=request.data)
#         if not serializers.is_valid():
#             return Response(data={'errors': serializers.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         DTDirector.name = request.data.get('name')
#         DTDirector.save()
#         return Response(data=DirectorSLZ(DTDirector).data)

class DirectorUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSLZ
    lookup_field = 'id'


# @api_view(['GET', 'PUT', 'DELETE'])
# def MovieDetail(request, id):
#     try:
#         DTMovie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data='MovieNotFound')
#     if request.method == 'GET':
#         data = MovieSLZ(DTMovie).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         DTMovie.delete()
#         return Response('no content')
#     elif request.method == 'PUT':
#         serializers = MovieCreateUpdateSerializer(data=request.data)
#         if not serializers.is_valid():
#             return Response(data={'errors': serializers.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         DTMovie.name = request.data.get('name')
#         DTMovie.save()
#         return Response(data=DirectorSLZ(DTMovie).data)

class MovieListDeleteUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSLZ
    lookup_field = 'id'



# @api_view(['GET'])
# def ReviewDetail(request, id):
#     try:
#         DTReview = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data='ReviewNotFound')
#     if request.method == 'GET':
#         data = ReviewSLZ(DTReview).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         DTReview.delete()
#         return Response('no content')
#     elif request.method == 'PUT':
#         serializers = ReviewCreateUpdateSerialiser(data=request.data)
#         if not serializers.is_valid():
#             return Response(data={'errors': serializers.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         DTReview.name = request.data.get('name')
#         DTReview.save()
#         return Response(data=DirectorSLZ(DTReview).data)
class ReviewListUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSLZ
    lookup_field = 'id'

# @api_view(['GET'])
# def listmiviewsbyreviews(request):
#     qeuryset = Movie.objects.all()
#     data = MovieSLZ(qeuryset).data
#     return Response(data=data)


# @api_view(['POST'])
# def authorization(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user =authenticate(username=username, password=password)
#         if user:
#             try:
#                 token = Token.objects.get(user=user)
#             except Token.DoesNotExist:
#                 token = Token.objects.create(user=user)
#             return Response(data={'key': token.key})
#         return Response(data={'errors': 'User not found'},
#                         status=status.HTTP_404_NOT_FOUND)

class AuthorizationAPIView(GenericAPIView):
    serializer_class = AuthorizationSerializer

    def post(self, request):
        serialiser = self.get_serializer(data=request.data)
        serialiser.is_valid(raise_exception=True)
        User.objects.create_user(**serialiser.validate_data)
        return Response(data={'message': 'Authorization'},
                        status=status.HTTP_200_OK)



class RegistrationAPIView(GenericAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        User.objects.create_user(**serializer.validate_data)
        return Response(data={'message': 'User created'},
                        status=status.HTTP_201_CREATED)



