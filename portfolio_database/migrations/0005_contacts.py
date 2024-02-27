# Generated by Django 2.2 on 2024-02-25 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_database', '0004_auto_20240218_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.CharField(max_length=200)),
                ('contact_message', models.CharField(max_length=1000)),
            ],
        ),
    ]