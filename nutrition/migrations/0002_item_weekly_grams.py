# Generated by Django 2.1.4 on 2018-12-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='weekly_grams',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=7),
        ),
    ]