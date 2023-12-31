# Generated by Django 4.2.3 on 2023-08-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_pal_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pal',
            name='age',
            field=models.IntegerField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='pal',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
