# Generated by Django 4.1.1 on 2022-10-06 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='ingrefientes',
            new_name='ingredientes',
        ),
    ]
