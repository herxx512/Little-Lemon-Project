# Generated by Django 5.0.1 on 2024-02-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_menu_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guests',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.SmallIntegerField(),
        ),
    ]