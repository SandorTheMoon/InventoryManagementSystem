# Generated by Django 5.0.4 on 2024-05-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0003_alter_product_category_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(default='Bread & Baked Goods', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_in_stock', models.IntegerField()),
                ('unit_of_measurement', models.CharField(max_length=50)),
                ('reorder_level', models.IntegerField()),
                ('supplier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Beverages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(default='Beverages', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_in_stock', models.IntegerField()),
                ('unit_of_measurement', models.CharField(max_length=50)),
                ('reorder_level', models.IntegerField()),
                ('supplier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Condiments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(default='Condiments & Sauces', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_in_stock', models.IntegerField()),
                ('unit_of_measurement', models.CharField(max_length=50)),
                ('reorder_level', models.IntegerField()),
                ('supplier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dairy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(default='Dairy Products', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_in_stock', models.IntegerField()),
                ('unit_of_measurement', models.CharField(max_length=50)),
                ('reorder_level', models.IntegerField()),
                ('supplier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(default='Dry Goods & Staples', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_in_stock', models.IntegerField()),
                ('unit_of_measurement', models.CharField(max_length=50)),
                ('reorder_level', models.IntegerField()),
                ('supplier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Meats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(default='Meats', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_in_stock', models.IntegerField()),
                ('unit_of_measurement', models.CharField(max_length=50)),
                ('reorder_level', models.IntegerField()),
                ('supplier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(default='Plastic/Paper & Packaging', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_in_stock', models.IntegerField()),
                ('unit_of_measurement', models.CharField(max_length=50)),
                ('reorder_level', models.IntegerField()),
                ('supplier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(default='Vegetable & Fruits', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_in_stock', models.IntegerField()),
                ('unit_of_measurement', models.CharField(max_length=50)),
                ('reorder_level', models.IntegerField()),
                ('supplier', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]