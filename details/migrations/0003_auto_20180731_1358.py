# Generated by Django 2.0.7 on 2018-07-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20180731_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailmodel',
            name='author',
            field=models.CharField(max_length=30, verbose_name='author'),
        ),
    ]
