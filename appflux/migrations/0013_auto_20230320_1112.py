# Generated by Django 3.2.13 on 2023-03-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appflux', '0012_auto_20230320_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(max_length=5000),
        ),
    ]
