# Generated by Django 4.1 on 2022-10-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='NIM',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='fakultas',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='nama',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='prodi',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='tanggal_lahir',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='staff',
            name='NIP',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='staff',
            name='alamat_rumah',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='staff',
            name='nama',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='staff',
            name='tanggal_lahir',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='staff',
            name='unit',
            field=models.CharField(max_length=200),
        ),
    ]
