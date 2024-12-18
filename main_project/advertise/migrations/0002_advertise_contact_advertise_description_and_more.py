# Generated by Django 5.1.4 on 2024-12-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='contact',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='advertise',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advertise',
            name='image',
            field=models.ImageField(null=True, upload_to='advertise/images'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='is_accepted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='advertise',
            name='is_approved',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='advertise',
            name='location',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='advertise',
            name='title',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
