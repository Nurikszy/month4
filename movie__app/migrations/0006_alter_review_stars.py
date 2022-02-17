# Generated by Django 4.0.2 on 2022-02-16 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie__app', '0005_alter_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.ForeignKey(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie__app.movie'),
        ),
    ]
