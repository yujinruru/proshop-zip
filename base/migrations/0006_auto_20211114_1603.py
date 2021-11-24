# Generated by Django 3.2.7 on 2021-11-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]