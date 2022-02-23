# Generated by Django 3.2.12 on 2022-02-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=60)),
                ('leavestart', models.DateField()),
                ('leaveend', models.DateField()),
                ('reason', models.TextField()),
                ('availibilty', models.CharField(max_length=20)),
                ('approval', models.CharField(choices=[('Y', 'Approved'), ('N', 'Not Approved')], max_length=40)),
                ('submitted', models.DateField(auto_now_add=True)),
            ],
        ),
    ]