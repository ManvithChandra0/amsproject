# Generated by Django 4.1.7 on 2023-03-31 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_delete_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='dateofbirth',
            new_name='type',
        ),
    ]
