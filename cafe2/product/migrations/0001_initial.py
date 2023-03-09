# Generated by Django 4.1.7 on 2023-03-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]