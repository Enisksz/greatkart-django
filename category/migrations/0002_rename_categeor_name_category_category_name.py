# Generated by Django 4.1.2 on 2022-10-07 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categeor_name',
            new_name='category_name',
        ),
    ]
