# Generated by Django 3.0.8 on 2020-08-01 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsstory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]