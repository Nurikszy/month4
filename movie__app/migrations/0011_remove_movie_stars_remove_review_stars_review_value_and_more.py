# Generated by Django 4.0.2 on 2022-02-18 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie__app', '0010_stars_review_stars_movie_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='stars',
        ),
        migrations.RemoveField(
            model_name='review',
            name='stars',
        ),
        migrations.AddField(
            model_name='review',
            name='value',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='movie__app.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Stars',
        ),
    ]
