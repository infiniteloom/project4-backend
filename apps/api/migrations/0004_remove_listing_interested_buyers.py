# Generated by Django 3.1.1 on 2020-09-15 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200915_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='interested_buyers',
        ),
    ]