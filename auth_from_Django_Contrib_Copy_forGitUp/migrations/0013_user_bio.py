# Generated by Django 2.2.6 on 2019-11-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_auto_20191021_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500, verbose_name='bio'),
        ),
    ]