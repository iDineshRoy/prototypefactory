# Generated by Django 4.0.3 on 2022-05-17 02:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_project_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(default='hello world'),
            preserve_default=False,
        ),
    ]
