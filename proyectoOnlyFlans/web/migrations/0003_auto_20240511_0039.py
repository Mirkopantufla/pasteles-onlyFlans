# Generated by Django 3.2.4 on 2024-05-11 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='ingredients',
            field=models.TextField(default='No ingredients'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flan',
            name='preparation',
            field=models.TextField(default='No preparation'),
            preserve_default=False,
        ),
    ]
