# Generated by Django 3.0.8 on 2020-07-29 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0003_auto_20200729_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
