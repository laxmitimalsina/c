# Generated by Django 3.1.4 on 2021-05-05 20:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0007_auto_20210428_1804'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Add_Section',
            new_name='CustomSection',
        ),
    ]
