# Generated by Django 2.2.4 on 2019-11-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0018_auto_20191129_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandas',
            name='Observacao',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
