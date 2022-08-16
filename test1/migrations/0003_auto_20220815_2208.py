# Generated by Django 3.2.8 on 2022-08-15 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_alter_fi_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fi',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fi',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]