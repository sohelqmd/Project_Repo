# Generated by Django 5.0.7 on 2024-07-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITApp', '0024_alter_itcontactinformation_office_hour_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itcontactinformation',
            name='office_hour_end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='itcontactinformation',
            name='office_hour_start',
            field=models.TimeField(),
        ),
    ]
