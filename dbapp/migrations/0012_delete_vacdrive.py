# Generated by Django 4.0.4 on 2022-05-24 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0011_alter_vacdosestatus_vacdated2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VacDrive',
        ),
    ]