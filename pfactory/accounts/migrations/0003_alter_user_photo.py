# Generated by Django 4.0.3 on 2022-06-06 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_address_user_education_user_phone_user_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
