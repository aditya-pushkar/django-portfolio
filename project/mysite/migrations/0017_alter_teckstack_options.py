# Generated by Django 3.2.5 on 2021-08-08 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_alter_teckstack_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teckstack',
            options={'ordering': ['-len_stack']},
        ),
    ]
