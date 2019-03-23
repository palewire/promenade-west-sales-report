# Generated by Django 2.1.7 on 2019-03-23 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('region', models.CharField(choices=[('Arts District', 'Arts District'), ('Bunker Hill', 'Bunker Hill'), ('City West', 'City West'), ('Fashion District', 'Fashion District'), ('Jewelry District', 'Jewelry District'), ('Financial District', 'Financial District'), ('Historic Core', 'Historic Core'), ('L.A. Live', 'L.A. Live'), ('Little Tokyo', 'Little Tokyo')], max_length=500)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]