# Generated by Django 5.0.3 on 2024-04-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/blog/post/', verbose_name='Imagen'),
        ),
    ]