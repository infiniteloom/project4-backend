# Generated by Django 3.1.1 on 2020-09-15 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200915_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(default='buyer', max_length=255),
        ),
    ]
