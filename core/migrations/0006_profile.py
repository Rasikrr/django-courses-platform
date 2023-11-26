# Generated by Django 4.2.7 on 2023-11-26 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to='profile_images')),
                ('website', models.URLField()),
                ('github', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('facebook', models.URLField()),
                ('address', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
