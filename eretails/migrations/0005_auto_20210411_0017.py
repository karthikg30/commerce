# Generated by Django 3.1.7 on 2021-04-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eretails', '0004_auto_20210411_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='date_modified',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='m_user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
