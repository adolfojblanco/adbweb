# Generated by Django 5.0.3 on 2024-03-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]