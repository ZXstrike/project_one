# Generated by Django 5.0.1 on 2024-01-09 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_members_member_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
