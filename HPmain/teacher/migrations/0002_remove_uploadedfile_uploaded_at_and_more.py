# Generated by Django 5.1 on 2024-09-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedfile',
            name='uploaded_at',
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='uploads/'),
        ),
    ]