# Generated by Django 4.1.2 on 2022-11-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_features_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='productName',
            field=models.CharField(default='', max_length=200),
        ),
    ]
