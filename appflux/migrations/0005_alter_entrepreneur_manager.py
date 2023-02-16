# Generated by Django 3.2.13 on 2023-02-15 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appflux', '0004_auto_20230215_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneur',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]