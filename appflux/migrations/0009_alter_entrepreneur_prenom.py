# Generated by Django 3.2.13 on 2023-02-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appflux', '0008_auto_20230215_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneur',
            name='prenom',
            field=models.CharField(max_length=30, verbose_name='prénom'),
        ),
    ]
