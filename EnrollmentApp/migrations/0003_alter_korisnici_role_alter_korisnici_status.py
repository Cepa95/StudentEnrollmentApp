# Generated by Django 4.2.1 on 2023-05-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnrollmentApp', '0002_alter_korisnici_role_alter_korisnici_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korisnici',
            name='role',
            field=models.CharField(choices=[('student', 'STUDENT'), ('administrator', 'ADMINISTRATOR'), ('profesor', 'PROFESOR')], default='student', max_length=20),
        ),
        migrations.AlterField(
            model_name='korisnici',
            name='status',
            field=models.CharField(choices=[('none', 'NONE'), ('redovan', 'REDOVAN'), ('izvanredan', 'IZVANREDAN')], default='none', max_length=20),
        ),
    ]
