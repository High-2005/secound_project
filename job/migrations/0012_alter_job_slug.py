# Generated by Django 4.2.2 on 2023-06-25 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_alter_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
