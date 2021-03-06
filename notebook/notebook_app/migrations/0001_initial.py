# Generated by Django 3.0.7 on 2021-02-26 12:14

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pinned', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=400)),
                ('description', tinymce.models.HTMLField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('color', models.CharField(choices=[('a', 'yellow'), ('b', 'white'), ('c', 'green'), ('d', 'red'), ('e', 'blue')], default='a', max_length=1)),
                ('tag', models.ManyToManyField(blank=True, to='notebook_app.Tags')),
            ],
            options={
                'ordering': ['-pinned', '-timestamp'],
            },
        ),
    ]
