# Generated by Django 3.1.3 on 2021-08-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_model_laws_data_imgfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
