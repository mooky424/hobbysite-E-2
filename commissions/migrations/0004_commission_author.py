# Generated by Django 5.0.2 on 2024-05-07 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0003_commission_status_job_jobapplication_delete_comment'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='user_management.profile'),
            preserve_default=False,
        ),
    ]