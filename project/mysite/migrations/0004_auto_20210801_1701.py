# Generated by Django 3.2.5 on 2021-08-01 11:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_portfolio_created_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg', 'jpeg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='teckstack',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg', 'jpeg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='teckstack',
            name='tech_title',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
