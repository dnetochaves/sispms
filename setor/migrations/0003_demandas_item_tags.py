# Generated by Django 2.2.4 on 2019-09-01 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0002_auto_20190814_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('Observacao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('Observacao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Demandas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Observacao', models.CharField(blank=True, max_length=50, null=True)),
                ('DataRegistro', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('ItemDemanda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ItemDemanda', to='setor.Item')),
                ('SetorDemanda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SetorDemanda', to='setor.Setor')),
                ('TagsDemandas', models.ManyToManyField(to='setor.Tags')),
            ],
        ),
    ]
