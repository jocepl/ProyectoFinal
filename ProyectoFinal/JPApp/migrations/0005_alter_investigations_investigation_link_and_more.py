# Generated by Django 4.1 on 2022-10-25 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPApp', '0004_alter_investigations_domain_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigations',
            name='investigation_link',
            field=models.URLField(verbose_name='Link de la investigación'),
        ),
        migrations.AlterField(
            model_name='tips',
            name='tips_link',
            field=models.URLField(verbose_name='Link del Refuerzo'),
        ),
    ]