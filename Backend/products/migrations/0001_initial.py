# Generated by Django 4.1.13 on 2024-02-13 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=255)),
                ('stock_status', models.CharField(choices=[('in_stock', 'In Stock'), ('out_of_stock', 'Out of Stock')], max_length=20)),
                ('available_stock', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
