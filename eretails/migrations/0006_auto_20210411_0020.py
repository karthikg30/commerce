# Generated by Django 3.1.7 on 2021-04-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eretails', '0005_auto_20210411_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='eretails.tags'),
        ),
    ]