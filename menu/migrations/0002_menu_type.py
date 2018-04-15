# Generated by Django 2.0.3 on 2018-04-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='type',
            field=models.CharField(choices=[('Горячее', '1'), ('Супы', '2'), ('Закуски', '3'), ('Напитки', '4')], default=1, max_length=1, verbose_name='Тип еды'),
            preserve_default=False,
        ),
    ]
