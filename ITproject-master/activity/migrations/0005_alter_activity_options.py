# Generated by Django 4.2.5 on 2024-03-14 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_activity_coasts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-id']},
        ),
    ]
