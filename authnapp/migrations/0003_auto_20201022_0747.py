# Generated by Django 2.2.16 on 2020-10-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0002_auto_20201022_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=20, verbose_name='возраст'),
        ),
    ]
