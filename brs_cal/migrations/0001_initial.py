# Generated by Django 4.0.6 on 2022-08-02 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, max_length=200, null=True)),
                ('remain_seat', models.IntegerField(blank=True, null=True)),
                ('f_month', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brs_cal.month')),
            ],
        ),
    ]
