# Generated by Django 3.1.1 on 2020-09-15 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20200915_0106'),
        ('api', '0004_remove_listing_interested_buyers'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='interested_buyers',
            field=models.ManyToManyField(null=True, related_name='interested_buyers', to='authentication.User'),
        ),
    ]