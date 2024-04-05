# Generated by Django 5.0.3 on 2024-04-01 11:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_company_taxes'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(default=1, max_length=50, verbose_name='País'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Localidad'),
            preserve_default=False,
        ),
    ]