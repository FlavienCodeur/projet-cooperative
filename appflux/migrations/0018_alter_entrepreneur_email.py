# Generated by Django 3.2.13 on 2023-03-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appflux', '0017_fichier_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneur',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
