# Generated by Django 3.1.2 on 2020-10-20 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='follow',
            table='Follows',
        ),
    ]
