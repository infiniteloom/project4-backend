# Generated by Django 3.1.1 on 2020-09-21 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='interested_buyers',
            field=models.ManyToManyField(blank=True, related_name='interested_buyers', to='authentication.User'),
        ),
        migrations.AddField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
        ),
    ]
