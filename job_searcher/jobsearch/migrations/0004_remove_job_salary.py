# Generated by Django 3.0.2 on 2020-01-26 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0003_auto_20200126_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='salary',
        ),
    ]