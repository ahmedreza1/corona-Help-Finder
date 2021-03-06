# Generated by Django 2.2.5 on 2020-04-29 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0003_mypost_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_num', models.IntegerField()),
                ('bank_name', models.CharField(max_length=240)),
                ('ifsc', models.CharField(max_length=240)),
                ('beneficiary_name', models.CharField(max_length=240)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid.MyProfile')),
            ],
        ),
    ]
