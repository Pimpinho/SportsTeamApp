# Generated by Django 5.1 on 2024-09-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportTeamApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='acronym',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Sigla'),
        ),
        migrations.AlterField(
            model_name='team',
            name='shortName',
            field=models.CharField(max_length=20, verbose_name='Abreviação'),
        ),
    ]