# Generated by Django 4.1.7 on 2023-02-18 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_remove_user_positive_review_positive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='positive',
            new_name='is_positive',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastName',
            new_name='last_name',
        ),
    ]