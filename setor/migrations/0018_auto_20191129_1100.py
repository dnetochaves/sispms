# Generated by Django 2.2.4 on 2019-11-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0017_tags_tagsetor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandas',
            name='Observacao',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
