# Generated by Django 2.1.4 on 2019-01-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0006_auto_20190104_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]