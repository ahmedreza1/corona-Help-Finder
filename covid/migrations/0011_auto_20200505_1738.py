# Generated by Django 2.2.5 on 2020-05-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0010_auto_20200505_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='mail',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
