# Generated by Django 3.1.7 on 2021-04-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('date_created', models.DateField(auto_created=True, null=True)),
                ('cust_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]