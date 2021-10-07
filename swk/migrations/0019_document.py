# Generated by Django 3.1.6 on 2021-09-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swk', '0018_supervisorslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
