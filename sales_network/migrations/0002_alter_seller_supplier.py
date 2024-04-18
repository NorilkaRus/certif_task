# Generated by Django 5.0.4 on 2024-04-14 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sales_network.seller', verbose_name='Поставщик'),
        ),
    ]