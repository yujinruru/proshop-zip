# Generated by Django 3.2.7 on 2021-10-02 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_imamge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imamge',
            new_name='image',
        ),
    ]
