# Generated by Django 5.0.1 on 2024-03-20 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='commissions.commission'),
        ),
    ]
