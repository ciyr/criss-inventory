# Generated by Django 4.1.2 on 2022-11-13 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_transaction_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
