# Generated by Django 3.1.2 on 2021-04-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_tender_api', '0012_auto_20210416_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='postedBy',
            field=models.CharField(default='', max_length=50),
        ),
    ]