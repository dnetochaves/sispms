# Generated by Django 2.2.4 on 2019-08-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_usuario_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_photo'),
        ),
    ]
