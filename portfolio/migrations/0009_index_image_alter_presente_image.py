# Generated by Django 4.2.3 on 2023-11-29 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_index_presente_tech0_tech1_textmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='presente',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
