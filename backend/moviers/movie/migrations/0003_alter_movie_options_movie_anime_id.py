# Generated by Django 4.0.3 on 2022-06-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_remove_movie_created_date_remove_movie_updated_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={},
        ),
        migrations.AddField(
            model_name='movie',
            name='anime_id',
            field=models.IntegerField(default=0),
        ),
    ]