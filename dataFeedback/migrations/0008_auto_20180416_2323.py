# Generated by Django 2.0.3 on 2018-04-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataFeedback', '0007_auto_20180416_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='alloperation_num',
            field=models.IntegerField(),
        ),
    ]
