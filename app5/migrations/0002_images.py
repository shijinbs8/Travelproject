# Generated by Django 3.2.15 on 2022-10-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='pics')),
                ('disc', models.TextField()),
            ],
        ),
    ]