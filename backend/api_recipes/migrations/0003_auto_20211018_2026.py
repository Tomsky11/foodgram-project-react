# Generated by Django 3.0.5 on 2021-10-18 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_recipes', '0002_auto_20211018_1857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipetags',
            options={'verbose_name': 'Теги', 'verbose_name_plural': 'Теги'},
        ),
    ]