# Generated by Django 4.2.1 on 2023-05-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]
