# Generated by Django 4.2.3 on 2023-08-01 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fib_webapp', '0002_alter_fibonaccitable_fib_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonaccitable',
            name='value',
            field=models.CharField(max_length=100),
        ),
    ]
