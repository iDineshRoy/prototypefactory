# Generated by Django 4.0.3 on 2022-05-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default='open', max_length=50, null=True),
        ),
    ]
