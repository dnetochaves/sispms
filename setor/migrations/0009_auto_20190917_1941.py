# Generated by Django 2.2.4 on 2019-09-17 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0008_auto_20190915_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandas',
            name='Observacao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
