# Generated by Django 2.0.3 on 2018-04-27 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataFeedback', '0012_auto_20180427_1553'),
    ]

    operations = [

        migrations.AlterField(
            model_name='state',
            name='process_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
