# Generated by Django 5.0.7 on 2024-07-31 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0002_rename_autormodel_autor'),
        ('genero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('data_lancamento', models.DateField(blank=True, null=True)),
                ('resumo', models.TextField(blank=True, null=True)),
                ('autor', models.ManyToManyField(related_name='filme', to='autor.autor')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='filme', to='genero.genero')),
            ],
        ),
    ]
