# Generated by Django 3.1.1 on 2020-09-17 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20200917_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='zip',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
