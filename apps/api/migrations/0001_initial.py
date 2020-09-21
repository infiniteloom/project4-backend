# Generated by Django 3.1.1 on 2020-09-21 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.IntegerField()),
                ('street', models.CharField(max_length=100)),
                ('year_built', models.IntegerField()),
                ('bed', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('home_size', models.IntegerField()),
                ('lot_size', models.FloatField()),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image1', models.TextField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
