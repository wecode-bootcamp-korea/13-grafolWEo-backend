# Generated by Django 3.1.2 on 2020-10-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20201022_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image_url',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
