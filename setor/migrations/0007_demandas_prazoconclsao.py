# Generated by Django 2.2.4 on 2019-09-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0006_auto_20190908_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandas',
            name='PrazoConclsao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data'),
        ),
    ]