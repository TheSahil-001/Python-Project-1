# Generated by Django 4.0.3 on 2022-03-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.FileField(default='images/Default.png', upload_to='Profile'),
        ),
    ]
