# Generated by Django 3.2.9 on 2021-11-30 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist_app', '0003_alter_tasklist_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
