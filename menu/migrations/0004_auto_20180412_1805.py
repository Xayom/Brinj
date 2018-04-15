# Generated by Django 2.0.3 on 2018-04-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20180412_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='img',
            field=models.ImageField(default=1, upload_to='images/', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='type',
            field=models.IntegerField(choices=[(1, 'Горячее'), (2, 'Супы'), (3, 'Закуски'), (4, 'Напитки')], verbose_name='Тип еды'),
        ),
    ]
