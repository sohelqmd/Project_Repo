# Generated by Django 5.0.7 on 2024-07-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITApp', '0027_itplacementdetails_mock_interview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinstitute',
            name='it_institute_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
