# Generated by Django 5.0.3 on 2024-04-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='taxes',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Impuesto'),
        ),
    ]
