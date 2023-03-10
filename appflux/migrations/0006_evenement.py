# Generated by Django 3.2.13 on 2023-03-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appflux', '0005_alter_rendezvous_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
                ('heure', models.DateTimeField()),
                ('compte_rendu', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('entrepreneurs', models.ManyToManyField(to='appflux.Entrepreneur')),
            ],
        ),
    ]
