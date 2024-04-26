# Generated by Django 5.0.4 on 2024-04-25 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_cliente_equipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_1_t1', models.CharField(max_length=200)),
                ('section_1_t2', models.CharField(max_length=200)),
                ('section_2_t1', models.TextField(null=True)),
                ('section_2_t2', models.TextField(null=True)),
                ('section_2_check1', models.CharField(max_length=100)),
                ('section_2_check2', models.CharField(max_length=100)),
                ('section_2_check3', models.CharField(max_length=100)),
                ('section_2_check4', models.CharField(max_length=100)),
                ('section_2_check5', models.CharField(max_length=100)),
                ('section_2_check6', models.CharField(max_length=100)),
                ('section_2_final', models.TextField(null=True)),
                ('section_4_t1', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteImagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, upload_to='galeria-cliente')),
                ('orden', models.IntegerField(default=1)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.cliente')),
            ],
            options={
                'verbose_name_plural': 'Fotos del Cliente',
                'db_table': 'tbl_cliente_imagen',
            },
        ),
        migrations.CreateModel(
            name='EquipoImagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, upload_to='galeria-equipo')),
                ('orden', models.IntegerField(default=1)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.equipo')),
            ],
            options={
                'verbose_name_plural': 'Imagenes del Equipo',
                'db_table': 'tbl_equipo_imagen',
            },
        ),
    ]