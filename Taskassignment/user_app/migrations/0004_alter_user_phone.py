# Generated by Django 4.2.4 on 2023-08-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
