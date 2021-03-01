# Generated by Django 3.0.5 on 2021-02-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(default=None, max_length=200)),
                ('caption', models.CharField(default=None, max_length=200)),
                ('published', models.BooleanField(default=False)),
                ('platform_to_publish', models.CharField(default=None, max_length=200)),
                ('date_to_be_published', models.DateField()),
            ],
        ),
    ]