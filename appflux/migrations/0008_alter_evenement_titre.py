# Generated by Django 3.2.13 on 2023-03-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appflux', '0007_auto_20230313_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='titre',
            field=models.CharField(max_length=20),
        ),
    ]
