# Generated by Django 3.1.6 on 2021-05-28 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swk', '0016_auto_20210519_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPictureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
    ]