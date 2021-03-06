# Generated by Django 3.2.5 on 2021-07-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=20)),
                ('website_link', models.URLField()),
                ('github_link', models.URLField()),
                ('tag1', models.CharField(max_length=15, null=True)),
                ('tag2', models.CharField(max_length=15, null=True)),
                ('tag3', models.CharField(max_length=15, null=True)),
                ('tag4', models.CharField(max_length=15, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TeckStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('tech_title', models.CharField(max_length=15)),
            ],
        ),
    ]
