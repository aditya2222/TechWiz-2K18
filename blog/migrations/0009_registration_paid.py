# Generated by Django 2.0.1 on 2018-01-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
