# Generated by Django 2.2.16 on 2020-10-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0003_auto_20201022_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(verbose_name='возраст'),
        ),
    ]