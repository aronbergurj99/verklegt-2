# Generated by Django 3.2 on 2021-05-14 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_searchhistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]