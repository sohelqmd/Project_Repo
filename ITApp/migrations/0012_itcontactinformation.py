# Generated by Django 5.0.7 on 2024-07-17 04:20

import django.core.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITApp', '0011_itplacementdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItContactInformation',
            fields=[
                ('it_contact_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('it_contact_person', models.CharField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN')),
                ('email_address', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Enter a valid email address')])),
                ('office_hour_start', models.TimeField(validators=[django.core.validators.MinValueValidator(limit_value='08:00'), django.core.validators.MaxValueValidator(limit_value='18:00')])),
                ('office_hour_end', models.TimeField(validators=[django.core.validators.MinValueValidator(limit_value='08:00'), django.core.validators.MaxValueValidator(limit_value='18:00')])),
                ('social_media_links', models.URLField(blank=True, validators=[django.core.validators.URLValidator(message='Enter a valid URL')])),
            ],
        ),
    ]
