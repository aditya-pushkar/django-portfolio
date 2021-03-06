# Generated by Django 3.2.5 on 2021-08-01 11:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20210801_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='teckstack',
            name='news_img',
            field=models.FileField(null=True, upload_to='static/images/%Y/%m/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])]),
        ),
        migrations.AlterField(
            model_name='teckstack',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
