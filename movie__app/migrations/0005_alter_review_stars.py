# Generated by Django 4.0.2 on 2022-02-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie__app', '0004_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100, null=True),
        ),
    ]
