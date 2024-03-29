# Generated by Django 5.0.2 on 2024-03-09 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miaplicacion', '0002_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
