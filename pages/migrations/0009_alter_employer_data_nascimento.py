# Generated by Django 4.0.6 on 2022-08-10 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_employer_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='data_nascimento',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
