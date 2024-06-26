# Generated by Django 5.0.3 on 2024-04-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/services/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
