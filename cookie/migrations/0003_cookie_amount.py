# Generated by Django 2.0.2 on 2019-12-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0002_cookie_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookie',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
