# Generated by Django 3.2.15 on 2022-08-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
    ]
