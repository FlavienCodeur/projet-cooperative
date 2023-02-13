# Generated by Django 3.2.13 on 2023-02-13 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('matricule', models.CharField(blank=True, max_length=30)),
                ('civilite', models.CharField(choices=[('Monsieur', 'Monsieur'), ('Madame', 'Madame'), ('Non defini', 'Non defini')], max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('email', models.CharField(max_length=150)),
            ],
        ),
    ]
