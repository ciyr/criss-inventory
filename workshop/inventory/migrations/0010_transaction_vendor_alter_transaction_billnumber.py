# Generated by Django 4.1.3 on 2023-01-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_remove_workorderitem_workorder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='vendor',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='billNumber',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
