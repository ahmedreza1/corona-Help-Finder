# Generated by Django 2.2.5 on 2020-05-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0007_mypost_donar_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='pic',
            field=models.URLField(blank=True, null=True),
        ),
    ]