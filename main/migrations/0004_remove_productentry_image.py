# Generated by Django 5.1.1 on 2024-09-17 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productentry_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productentry',
            name='image',
        ),
    ]
