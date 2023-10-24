# Generated by Django 4.2.6 on 2023-10-22 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docs', '0002_alter_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='enrollment_no',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]