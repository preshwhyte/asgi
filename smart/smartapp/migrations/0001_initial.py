# Generated by Django 4.0.6 on 2022-09-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('other', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.TextField()),
                ('phone', models.IntegerField(max_length=15)),
            ],
        ),
    ]
