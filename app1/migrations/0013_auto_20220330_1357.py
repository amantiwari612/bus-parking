# Generated by Django 2.2 on 2022-03-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20220330_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='seat',
        ),
        migrations.AddField(
            model_name='seat',
            name='nos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seat',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]