# Generated by Django 4.0.2 on 2022-02-17 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie__app', '0007_alter_review_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STARS', models.CharField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie__app.stars'),
        ),
    ]
