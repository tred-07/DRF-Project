# Generated by Django 5.1.4 on 2024-12-18 20:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advertise', '0004_alter_advertise_is_accepted_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=40)),
                ('comment', models.CharField(max_length=40)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('advertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertise.advertise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userReview', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]