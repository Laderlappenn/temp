# Generated by Django 4.0.4 on 2023-03-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
