from django.contrib import admin
from movie__app.models import Director
from movie__app.models import Movie
from movie__app.models import Review
# Register your models here.
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)
