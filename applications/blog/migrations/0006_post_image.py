# Generated by Django 5.0.3 on 2024-04-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_created_on_post_create_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=2, upload_to='images/blog/post/', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]