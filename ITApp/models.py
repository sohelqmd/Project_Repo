from django.db import models

# Create your models here.
from django.core.validators import URLValidator, MinValueValidator, MaxValueValidator, EmailValidator, RegexValidator, MinLengthValidator, MaxLengthValidator
from django.utils import timezone
from datetime import date,timedelta,time
from phonenumber_field.modelfields import PhoneNumberField


class ItInstitute(models.Model):
    It_id = models.PositiveIntegerField(primary_key=True)
    it_institute_name = models.CharField(max_length=255,unique=True)
    summary = models.TextField()
    established_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1800), 
            MaxValueValidator(timezone.now().year)
        ],
        help_text="Enter a valid year"
    )
    website_url = models.URLField(validators=[URLValidator()], null=True)
    accreditation_details = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    affiliations = models.TextField(blank=True, null=True)
    achievements_and_awards = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.it_institute_name
    
class ItContactInformation(models.Model):
    it_contact_id = models.PositiveIntegerField(primary_key=True)
    it_institute = models.ForeignKey(ItInstitute, null=True,  on_delete=models.CASCADE)
    it_contact_person = models.CharField(max_length=100)
    phone_number = PhoneNumberField(region='IN')  # Uses django-phonenumber-field for international phone number validation
    email_address = models.EmailField(validators=[EmailValidator(message="Enter a valid email address")], )
    office_hour_start = models.TimeField()
    office_hour_end = models.TimeField()
    social_media_links = models.URLField(validators=[URLValidator(message="Enter a valid URL")], blank=True)  # Optional field

    def __str__(self):
        return self.it_contact_person
    
class ItLocationInformation(models.Model):
    it_location_id = models.PositiveIntegerField(primary_key=True)
    it_institute = models.ForeignKey(ItInstitute, null=True,  on_delete=models.CASCADE)
    address = models.CharField(
        max_length=255,
        validators=[
            MinLengthValidator(5, message='Address should be at least 5 characters long.'),
            RegexValidator(
                regex=r'^[0-9a-zA-Z\s\.,#-]+$',
                message='Address should only contain alphanumeric characters, spaces, dots, commas, dashes, and hash symbols.',
                code='invalid_address'
            )
        ]
    )
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(
                regex=r'^\d{6}$',
                message='PIN code must be exactly 6 digits.',
                code='invalid_pin_code'
            )
        ]
    )
    nearby_landmarks = models.TextField(blank=True)

    def __str__(self):
        return self.city
    
class It_Course_Chocies(models.Model):
    it_course_no = models.PositiveIntegerField(primary_key=True)
    it_course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.it_course_name
    
class ItCourseForm(models.Model):

    COURSE_MODE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('both', 'Both')
    ]
    it_course_id = models.PositiveIntegerField(primary_key=True)
    it_institute = models.ForeignKey(ItInstitute, on_delete=models.CASCADE)
    it_courses = models.ForeignKey(It_Course_Chocies, on_delete=models.CASCADE)
    duration_days = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(365)],
        help_text="Enter duration in days (1-365)"
    )
    duration = models.DurationField(
        default=timedelta(hours=1),
        help_text="Enter duration (HH:MM:SS)"
    )
    fee_range = models.CharField(max_length=100)
    class_timing_start = models.TimeField(
        default=time(9, 0),
        help_text="Enter the start time (HH:MM)"
    )
    class_timing_end = models.TimeField(
        default=time(17, 0),
        help_text="Enter the end time (HH:MM)"
    )
    batch_size = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Enter a valid batch size"
    )
    batch_start_date = models.DateField(default=date.today)
    demo_classes_available = models.BooleanField(default=False)
    demo_date = models.DateField(default=date.today, blank=True, null=True)
    certification_details = models.TextField( blank=True, null=True)
    mode_of_instruction = models.CharField(max_length=10, choices=COURSE_MODE_CHOICES, default='online')
    language_of_instruction = models.CharField(max_length=50, blank=True, null=True)

    
class ItTrainer(models.Model):
    It_trainer_id = models.PositiveIntegerField(primary_key=True)
    it_institute = models.ForeignKey(ItInstitute, on_delete=models.CASCADE)
    it_courses = models.ForeignKey(It_Course_Chocies, on_delete=models.CASCADE)
    it_trainer_name = models.CharField(max_length=255)
    qualifications = models.CharField(max_length=255)
    experience_years = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Enter a valid number of years"
    )
    specializations = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.it_trainer_name

class ItPlacementDetails(models.Model):
    It_Placement_id = models.PositiveIntegerField(primary_key=True)
    it_institute = models.ForeignKey(ItInstitute, null=True, on_delete=models.CASCADE)
    placement_statistics = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Enter placement success rate (%)"
    )
    placement_count = models.PositiveIntegerField(null=True)
    companies_associated = models.TextField(
        null=True,
        blank=True,
        help_text="Enter names of companies associated with placements"
    )
    placement_process = models.TextField(
        null=True,
        blank=True,
        help_text="Describe the placement process"
    )
    mock_interview = models.BooleanField(default=False)
    mock_test = models.BooleanField(default=False)
    softskills  = models.BooleanField(default=False)
    success_stories = models.TextField(
        null=True,
        blank=True,
        help_text="Share success stories or testimonials"
    )
    internship_opportunities = models.TextField(
        null=True,
        blank=True,
        help_text="Describe internship opportunities"
    )

    #def __str__(self):
        #return self.placement_statistics


class ItFacilitiesAndInfrastructure(models.Model):
    it_facilities_id = models.PositiveIntegerField(primary_key=True)
    it_institute = models.ForeignKey(ItInstitute, null=True,  on_delete=models.CASCADE)
    classroom_facilities = models.TextField(blank=True, null=True)
    lab_facilities = models.TextField(blank=True, null=True)
    library = models.TextField(blank=True, null=True)
    safety_and_security_measures = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.classroom_facilities
    
class ItAdmissionProcess(models.Model):
    it_admission_id = models.PositiveIntegerField(primary_key=True)
    it_institute = models.ForeignKey(ItInstitute, null=True,  on_delete=models.CASCADE)
    admission_requirements = models.TextField()
    application_process = models.TextField()
    application_start = models.DateField(
        help_text='Format: YYYY-MM-DD',
        validators=[
            RegexValidator(
                regex=r'^\d{4}-\d{2}-\d{2}$',
                message='Date must be in the format YYYY-MM-DD.',
                code='invalid_date_format'
            )
        ]
    )
    application_deadline = models.DateField(
        help_text='Format: YYYY-MM-DD',
        validators=[
            RegexValidator(
                regex=r'^\d{4}-\d{2}-\d{2}$',
                message='Date must be in the format YYYY-MM-DD.',
                code='invalid_date_format'
            )
        ]
    )
    exam_date = models.DateField(
        help_text='Format: YYYY-MM-DD',
        validators=[
            RegexValidator(
                regex=r'^\d{4}-\d{2}-\d{2}$',
                message='Date must be in the format YYYY-MM-DD.',
                code='invalid_date_format'
            )
        ]
    )
    admission_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0, message='Admission fee cannot be negative.'),
            MaxValueValidator(1000000, message='Admission fee exceeds maximum allowed amount.')
        ]
    )
    scholarships = models.TextField(blank=True, null=True)
    entrance_exams_accepted = models.CharField(max_length=100,blank=True,null=True)
    interview_process = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.admission_requirements

class ItContactAndSupportForm(models.Model):
    it_support_id = models.PositiveIntegerField(primary_key=True)
    it_institute = models.ForeignKey(ItInstitute, null=True,  on_delete=models.CASCADE)
    it_support_person = models.CharField(max_length=100)
    phone_number = PhoneNumberField(region='IN')  # Uses django-phonenumber-field for international phone number validation
    email_address = models.EmailField(validators=[EmailValidator(message="Enter a valid email address")], )
    office_hour_start = models.TimeField(
        validators=[
            MinValueValidator(limit_value='08:00'),  # Example: Minimum time allowed (e.g., 08:00)
            MaxValueValidator(limit_value='18:00')   # Example: Maximum time allowed (e.g., 18:00)
        ]
    )
    office_hour_end = models.TimeField(
        validators=[
            MinValueValidator(limit_value='08:00'),  # Example: Minimum time allowed (e.g., 08:00)
            MaxValueValidator(limit_value='18:00')   # Example: Maximum time allowed (e.g., 18:00)
        ]
    )
    support_services = models.TextField(blank=True,null=True)
    faqs = models.TextField(blank=True,null=True)

class ItAdditionalInformation(models.Model):
    it_additional_id = models.PositiveIntegerField(primary_key=True)
    it_institute = models.ForeignKey(ItInstitute, null=True,  on_delete=models.CASCADE)
    other_social_media_links = models.URLField(validators=[URLValidator()], blank=True, null=True)
    events_seminars = models.TextField(blank=True,null=True)
    news_updates = models.TextField(blank=True,null=True)

    #def __str__(self):
        #return self.it_additional_id

