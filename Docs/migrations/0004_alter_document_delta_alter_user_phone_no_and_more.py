# Generated by Django 4.2.6 on 2023-12-13 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Docs', '0003_alter_document_delta_alter_document_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='delta',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(blank=True, default='00', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='useraccess',
            name='for_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='useraccess',
            unique_together={('for_user', 'document')},
        ),
    ]