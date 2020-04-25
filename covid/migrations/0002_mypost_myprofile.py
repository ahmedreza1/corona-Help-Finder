# Generated by Django 2.2.5 on 2020-04-22 15:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('covid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('address', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('LGBTQ', 'LGBTQ')], default='Male', max_length=20)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('description', models.CharField(blank=True, max_length=240, null=True)),
                ('pic', models.ImageField(null=True, upload_to='image\\')),
                ('donation_given', models.IntegerField(blank=True, null=True)),
                ('donation_recived', models.IntegerField(blank=True, null=True)),
                ('purpose', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_one', models.ImageField(null=True, upload_to='image\\')),
                ('pic_two', models.ImageField(null=True, upload_to='image\\')),
                ('pic_three', models.ImageField(null=True, upload_to='image\\')),
                ('pic_four', models.ImageField(null=True, upload_to='image\\')),
                ('pic_five', models.ImageField(null=True, upload_to='image\\')),
                ('main_pic', models.ImageField(null=True, upload_to='image\\')),
                ('amount_spend', models.IntegerField(blank=True, null=True)),
                ('total_donars', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='covid.MyProfile')),
            ],
        ),
    ]
