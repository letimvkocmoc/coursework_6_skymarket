# Generated by Django 3.2.6 on 2023-05-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, help_text='Разместите фото для объявления', null=True, upload_to='images/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
    ]