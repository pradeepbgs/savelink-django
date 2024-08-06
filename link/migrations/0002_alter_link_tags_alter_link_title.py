# Generated by Django 5.0.7 on 2024-08-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='tags',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
