# Generated by Django 3.2 on 2021-04-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_data',
            name='document',
            field=models.FileField(default=0, upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee_data',
            name='phone_no',
            field=models.CharField(max_length=20),
        ),
    ]
