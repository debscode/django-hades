# Generated by Django 3.1.3 on 2020-11-26 02:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombres')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='joined_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 25, 21, 47, 34, 131790), verbose_name='Fecha de registro'),
        ),
        migrations.AddField(
            model_name='employee',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='erp.type'),
        ),
    ]
