# Generated by Django 4.0.3 on 2022-05-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_result1_remove_contact_full_name_contact_last_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result1',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
