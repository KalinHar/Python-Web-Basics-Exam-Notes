# Generated by Django 4.0.2 on 2022-02-20 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('title',)},
        ),
    ]
