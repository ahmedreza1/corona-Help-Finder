# Generated by Django 2.2.5 on 2020-05-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0006_fakecheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='donar_names',
            field=models.TextField(default='ahmed'),
            preserve_default=False,
        ),
    ]