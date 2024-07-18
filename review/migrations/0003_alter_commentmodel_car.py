# Generated by Django 5.0.4 on 2024-07-15 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_carmodel_owner'),
        ('review', '0002_alter_commentmodel_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cars.carmodel'),
        ),
    ]
