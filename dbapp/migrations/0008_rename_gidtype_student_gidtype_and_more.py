# Generated by Django 4.0.2 on 2022-02-17 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0007_remove_vacdrive_id_alter_vacdosestatus_sid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='gIDType',
            new_name='gidtype',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='mobileNum',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='fName',
            new_name='sfname',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='lName',
            new_name='slname',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='vacPref',
            new_name='vaccine',
        ),
    ]
