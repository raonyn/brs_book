# Generated by Django 4.0.6 on 2022-07-28 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brs_app', '0003_alter_brsbook_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='brsbook',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]