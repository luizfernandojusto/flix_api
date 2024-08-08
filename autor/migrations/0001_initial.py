# Generated by Django 5.0.7 on 2024-07-30 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('nacionalidade', models.CharField(blank=True, choices=[('USA', 'Estado Unidos'), ('BRASIL', 'Brasil')], max_length=100, null=True)),
            ],
        ),
    ]
