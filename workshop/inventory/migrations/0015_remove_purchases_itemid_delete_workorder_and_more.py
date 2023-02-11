# Generated by Django 4.1.3 on 2023-02-11 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_rename_completeiondate_workorder_completiondate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchases',
            name='itemId',
        ),
        migrations.DeleteModel(
            name='WorkOrder',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='cost',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='issuee',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='Purchases',
        ),
    ]