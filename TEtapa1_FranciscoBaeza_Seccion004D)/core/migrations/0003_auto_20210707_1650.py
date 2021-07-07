# Generated by Django 3.2.3 on 2021-07-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210707_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='detalles',
            field=models.CharField(max_length=150, verbose_name='detalles'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='email',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='nombre'),
        ),
    ]