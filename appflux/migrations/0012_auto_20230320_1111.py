# Generated by Django 3.2.13 on 2023-03-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appflux', '0011_alter_answer_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(max_length=1500),
        ),
    ]