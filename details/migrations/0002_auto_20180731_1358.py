# Generated by Django 2.0.7 on 2018-07-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailmodel',
            name='author',
            field=models.CharField(default='', max_length=30, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='detailmodel',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
