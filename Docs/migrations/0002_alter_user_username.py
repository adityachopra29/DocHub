# Generated by Django 4.2.5 on 2023-10-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
