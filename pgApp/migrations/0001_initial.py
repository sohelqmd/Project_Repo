# Generated by Django 5.0.7 on 2024-07-18 04:54

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PG_Course_Chocies',
            fields=[
                ('PG_course_no', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('PG_course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PGInstitute',
            fields=[
                ('PG_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('PG_institute_name', models.CharField(max_length=255)),
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
        migrations.CreateModel(
            name='PGFacilitiesAndInfrastructure',
            fields=[
                ('PG_facilities_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('classroom_facilities', models.TextField(blank=True, null=True)),
                ('lab_facilities', models.TextField(blank=True, null=True)),
                ('library', models.TextField(blank=True, null=True)),
                ('safety_and_security_measures', models.TextField(blank=True, null=True)),
                ('PG_institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pgApp.pginstitute')),
            ],
        ),
        migrations.CreateModel(
            name='PGCourseForm',
            fields=[
                ('PG_course_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('duration_days', models.IntegerField(help_text='Enter duration in days (1-365)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(365)])),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=3600), help_text='Enter duration (HH:MM:SS)')),
                ('fee_range', models.CharField(max_length=100)),
                ('class_timing_start', models.TimeField(default=datetime.time(9, 0), help_text='Enter the start time (HH:MM)')),
                ('class_timing_end', models.TimeField(default=datetime.time(17, 0), help_text='Enter the end time (HH:MM)')),
                ('batch_size', models.PositiveIntegerField(help_text='Enter a valid batch size', validators=[django.core.validators.MinValueValidator(1)])),
                ('batch_start_date', models.DateField(default=datetime.date.today)),
                ('demo_classes_available', models.BooleanField(default=False)),
                ('demo_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('certification_details', models.TextField(blank=True, null=True)),
                ('mode_of_instruction', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline'), ('both', 'Both')], default='online', max_length=10)),
                ('language_of_instruction', models.CharField(blank=True, max_length=50, null=True)),
                ('PG_courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgApp.pg_course_chocies')),
                ('PG_institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgApp.pginstitute')),
            ],
        ),
        migrations.CreateModel(
            name='PGContactInformation',
            fields=[
                ('PG_contact_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('PG_contact_person', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Enter a valid email address')])),
                ('office_hour_start', models.TimeField()),
                ('office_hour_end', models.TimeField()),
                ('social_media_links', models.URLField(blank=True, validators=[django.core.validators.URLValidator(message='Enter a valid URL')])),
                ('PG_institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pgApp.pginstitute')),
            ],
        ),
        migrations.CreateModel(
            name='PGContactAndSupportForm',
            fields=[
                ('PG_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('PG_support_person', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Enter a valid email address')])),
                ('office_hour_start', models.TimeField(validators=[django.core.validators.MinValueValidator(limit_value='08:00'), django.core.validators.MaxValueValidator(limit_value='18:00')])),
                ('office_hour_end', models.TimeField(validators=[django.core.validators.MinValueValidator(limit_value='08:00'), django.core.validators.MaxValueValidator(limit_value='18:00')])),
                ('support_services', models.TextField(blank=True, null=True)),
                ('faqs', models.TextField(blank=True, null=True)),
                ('PG_institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pgApp.pginstitute')),
            ],
        ),
        migrations.CreateModel(
            name='PGAdmissionProcess',
            fields=[
                ('PG_admission_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('admission_requirements', models.TextField()),
                ('application_process', models.TextField()),
                ('application_start', models.DateField(help_text='Format: YYYY-MM-DD', validators=[django.core.validators.RegexValidator(code='invalid_date_format', message='Date must be in the format YYYY-MM-DD.', regex='^\\d{4}-\\d{2}-\\d{2}$')])),
                ('application_deadline', models.DateField(help_text='Format: YYYY-MM-DD', validators=[django.core.validators.RegexValidator(code='invalid_date_format', message='Date must be in the format YYYY-MM-DD.', regex='^\\d{4}-\\d{2}-\\d{2}$')])),
                ('exam_date', models.DateField(help_text='Format: YYYY-MM-DD', validators=[django.core.validators.RegexValidator(code='invalid_date_format', message='Date must be in the format YYYY-MM-DD.', regex='^\\d{4}-\\d{2}-\\d{2}$')])),
                ('admission_fee', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0, message='Admission fee cannot be negative.'), django.core.validators.MaxValueValidator(1000000, message='Admission fee exceeds maximum allowed amount.')])),
                ('scholarships', models.TextField(blank=True, null=True)),
                ('entrance_exams_accepted', models.CharField(blank=True, max_length=100, null=True)),
                ('interview_process', models.TextField(blank=True, null=True)),
                ('PG_institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pgApp.pginstitute')),
            ],
        ),
        migrations.CreateModel(
            name='PGAdditionalInformation',
            fields=[
                ('PG_additional_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('other_social_media_links', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('events_seminars', models.TextField(blank=True, null=True)),
                ('news_updates', models.TextField(blank=True, null=True)),
                ('PG_institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pgApp.pginstitute')),
            ],
        ),
        migrations.CreateModel(
            name='PGLocationInformation',
            fields=[
                ('PG_location_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(5, message='Address should be at least 5 characters long.'), django.core.validators.RegexValidator(code='invalid_address', message='Address should only contain alphanumeric characters, spaces, dots, commas, dashes, and hash symbols.', regex='^[0-9a-zA-Z\\s\\.,#-]+$')])),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(code='invalid_pin_code', message='PIN code must be exactly 6 digits.', regex='^\\d{6}$')])),
                ('nearby_landmarks', models.TextField(blank=True)),
                ('PG_institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pgApp.pginstitute')),
            ],
        ),
        migrations.CreateModel(
            name='PGTopranks',
            fields=[
                ('PG_topranks_id', models.IntegerField(primary_key=True, serialize=False)),
                ('success_rate', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Placed_student_Name', models.CharField(max_length=50, null=True)),
                ('test_name', models.CharField(max_length=50, null=True)),
                ('rank_scored', models.CharField(max_length=255)),
                ('placed_year', models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2024)])),
                ('success_stories', models.TextField(blank=True, null=True)),
                ('UG_institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgApp.pginstitute')),
            ],
        ),
        migrations.CreateModel(
            name='PGTrainer',
            fields=[
                ('PG_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('PG_trainer_name', models.CharField(max_length=255)),
                ('qualifications', models.CharField(max_length=255)),
                ('experience_years', models.IntegerField(help_text='Enter a valid number of years', validators=[django.core.validators.MinValueValidator(0)])),
                ('specializations', models.TextField(blank=True, null=True)),
                ('achievements', models.TextField(blank=True, null=True)),
                ('PG_courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgApp.pg_course_chocies')),
                ('PG_institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgApp.pginstitute')),
            ],
        ),
    ]
