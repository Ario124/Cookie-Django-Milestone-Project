# Generated by Django 2.0.2 on 2019-12-07 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='makeorder',
            old_name='county',
            new_name='street_address',
        ),
        migrations.RemoveField(
            model_name='makeorder',
            name='street_address1',
        ),
        migrations.RemoveField(
            model_name='makeorder',
            name='street_address2',
        ),
    ]
