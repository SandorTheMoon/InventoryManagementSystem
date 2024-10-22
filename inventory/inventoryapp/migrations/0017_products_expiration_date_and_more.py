# Generated by Django 5.0.4 on 2024-06-06 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0016_alter_purchaseorder_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_status',
            field=models.CharField(blank=True, choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accept'), ('REJECTED', 'Reject')], max_length=20, null=True),
        ),
    ]
