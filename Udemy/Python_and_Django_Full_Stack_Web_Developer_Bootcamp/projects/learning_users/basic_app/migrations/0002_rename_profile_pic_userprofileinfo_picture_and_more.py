# Generated by Django 4.0 on 2022-01-06 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pic',
            new_name='picture',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_site',
            new_name='portfolio',
        ),
    ]
