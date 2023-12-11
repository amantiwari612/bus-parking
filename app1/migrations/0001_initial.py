# Generated by Django 4.0.2 on 2022-03-08 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('timing', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=800, null=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.IntegerField()),
                ('price', models.IntegerField()),
                ('booked', models.BooleanField(default=True)),
                ('timing', models.DateTimeField(blank=True, null=True)),
                ('booked_by_user', models.CharField(max_length=200)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.busdetail')),
            ],
        ),
    ]