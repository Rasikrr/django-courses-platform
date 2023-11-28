# Generated by Django 4.2.7 on 2023-11-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_profilemodel_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='specialization',
            field=models.CharField(blank=True, choices=[('backend', 'Backend Developer'), ('frontend', 'Frontend Developer'), ('fullstack', 'Full Stack Developer'), ('android', 'Mobile Android Developer'), ('ios', 'Mobile IOS Developer'), ('gamedev', 'Game Developer')], default=None, max_length=100, null=True),
        ),
    ]
