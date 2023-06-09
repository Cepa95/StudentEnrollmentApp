# Generated by Django 4.2.1 on 2023-05-23 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EnrollmentApp', '0007_alter_predmeti_nositelj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predmeti',
            name='izborni',
            field=models.CharField(choices=[('da', 'da'), ('ne', 'ne')], max_length=10),
        ),
        migrations.CreateModel(
            name='StudentEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Enrolled', 'ENROLLED'), ('Passed', 'PASSED'), ('Failed', 'FAILED')], max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EnrollmentApp.predmeti')),
            ],
        ),
    ]
