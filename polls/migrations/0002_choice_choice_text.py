# Generated by Django 2.2.9 on 2020-01-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
