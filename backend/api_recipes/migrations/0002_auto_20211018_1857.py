# Generated by Django 3.0.5 on 2021-10-18 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipetags',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
