# Generated by Django 5.1.2 on 2024-11-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='base_value',
        ),
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]