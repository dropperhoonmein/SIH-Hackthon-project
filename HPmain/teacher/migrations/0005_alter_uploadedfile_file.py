# Generated by Django 5.1 on 2024-09-06 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_topic_topic_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='HPmain/media/uploads/'),
        ),
    ]