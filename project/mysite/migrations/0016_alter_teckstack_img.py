# Generated by Django 3.2.5 on 2021-08-08 12:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_alter_teckstack_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teckstack',
            name='img',
            field=models.FileField(null=True, upload_to='techstack/', validators=[django.core.validators.FileExtensionValidator(['jpeg', 'png', 'svg'])]),
        ),
    ]
