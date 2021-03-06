# Generated by Django 4.0.1 on 2022-01-17 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invi_code', models.IntegerField()),
                ('bio', models.CharField(max_length=500, null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='pics')),
                ('twitter', models.URLField(null=True)),
                ('facebook', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('linkedin', models.URLField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
