# Generated by Django 4.0.2 on 2022-02-17 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie__app', '0009_remove_review_stars_delete_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie__app.movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='stars',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie__app.stars'),
        ),
    ]
