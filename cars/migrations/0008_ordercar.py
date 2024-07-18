# Generated by Django 5.0.4 on 2024-07-16 12:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_carmodel_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Buyer name')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel', verbose_name='ordered car')),
            ],
        ),
    ]
