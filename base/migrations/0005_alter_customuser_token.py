# Generated by Django 5.0.3 on 2024-05-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_customuser_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='token',
            field=models.CharField(default=False, max_length=256),
        ),
    ]