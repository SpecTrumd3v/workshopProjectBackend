# Generated by Django 3.2.9 on 2021-12-13 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reception_date', models.DateField(auto_now=True)),
                ('deliver_date', models.DateField()),
            ],
        ),
    ]
