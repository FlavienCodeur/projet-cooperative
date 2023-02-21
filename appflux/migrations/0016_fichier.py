# Generated by Django 3.2.13 on 2023-02-20 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appflux', '0015_remove_entrepreneur_attestation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fichier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('fichier', models.FileField(upload_to='fichiers/')),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appflux.entrepreneur')),
            ],
        ),
    ]