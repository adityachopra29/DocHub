# Generated by Django 4.2.6 on 2023-10-22 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docs', '0003_users_enrollment_no_alter_users_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone_no',
            field=models.BigIntegerField(),
        ),
    ]