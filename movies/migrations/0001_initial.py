# Generated by Django 5.1.4 on 2024-12-10 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('release_year', models.IntegerField()),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
    ]
