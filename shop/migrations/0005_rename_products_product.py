# Generated by Django 3.2.7 on 2021-09-08 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='product',
        ),
    ]
