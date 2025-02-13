# Generated by Django 5.0.7 on 2024-07-16 12:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItInstitute',
            fields=[
                ('It_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('it_institute_name', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('established_year', models.PositiveIntegerField(help_text='Enter a valid year', validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2024)])),
                ('website_url', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('accreditation_details', models.TextField(blank=True, null=True)),
                ('mission', models.TextField(blank=True, null=True)),
                ('vision', models.TextField(blank=True, null=True)),
                ('affiliations', models.TextField(blank=True, null=True)),
                ('achievements_and_awards', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
