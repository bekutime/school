# Generated by Django 4.0.6 on 2022-07-06 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0002_alter_student_date_of_birth_alter_student_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='owner',
            new_name='courses',
        ),
    ]
