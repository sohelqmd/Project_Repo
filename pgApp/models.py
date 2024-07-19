from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import URLValidator, MinValueValidator, MaxValueValidator,EmailValidator, RegexValidator, MinLengthValidator, MaxLengthValidator
from django.utils import timezone
from datetime import date,timedelta,time

# Create your models here.

class PGInstitute(models.Model):
    PG_id = models.PositiveIntegerField(primary_key=True)
    PG_institute_name = models.CharField(max_length=255)
    summary = models.TextField()
    established_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1800), 
            MaxValueValidator(timezone.now().year)
        ],
        help_text="Enter a valid year"
    )
    website_url = models.URLField(validators=[URLValidator()], blank=True, null=True)
    accreditation_details = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    affiliations = models.TextField(blank=True, null=True)
    achievements_and_awards = models.TextField(blank=True, null=True)

    def str(self):
        return self.PG_institute_name
    
class PGContactInformation(models.Model):
    PG_contact_id = models.PositiveIntegerField(primary_key=True)
    PG_institute = models.ForeignKey(PGInstitute, null=True,  on_delete=models.CASCADE)
    PG_contact_person = models.CharField(max_length=100)
    email_address = models.EmailField(validators=[EmailValidator(message="Enter a valid email address")], )
    office_hour_start = models.TimeField()
    office_hour_end = models.TimeField()
    social_media_links = models.URLField(validators=[URLValidator(message="Enter a valid URL")], blank=True)  # Optional field

    def str(self):
        return self.PG_contact_person
    




    
class PGLocationInformation(models.Model):
    PG_location_id = models.PositiveIntegerField(primary_key=True)
    PG_institute = models.ForeignKey(PGInstitute, null=True,  on_delete=models.CASCADE)
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

    def str(self):
        return self.city
    
class PG_Course_Chocies(models.Model):
    PG_course_no = models.PositiveIntegerField(primary_key=True)
    PG_course_name = models.CharField(max_length=50)

    def str(self):
        return self.PG_course_name
    
class PGCourseForm(models.Model):

    COURSE_MODE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('both', 'Both')
    ]
    PG_course_id = models.PositiveIntegerField(primary_key=True)
    PG_institute = models.ForeignKey(PGInstitute, on_delete=models.CASCADE)
    PG_courses = models.ForeignKey(PG_Course_Chocies, on_delete=models.CASCADE)
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

    #def str(self):
        #return self.PG_courses
    







class PGTrainer(models.Model):
    PG_id = models.PositiveIntegerField(primary_key=True)
    PG_institute = models.ForeignKey(PGInstitute, on_delete=models.CASCADE)
    PG_courses = models.ForeignKey(PG_Course_Chocies, on_delete=models.CASCADE)
    PG_trainer_name = models.CharField(max_length=255)
    qualifications = models.CharField(max_length=255)
    experience_years = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Enter a valid number of years"
    )
    specializations = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)

    def str(self):
        return self.PG_trainer_name
    



class PGTopranks(models.Model):
    PG_topranks_id=models.IntegerField(primary_key=True)
    UG_institute=models.ForeignKey(PGInstitute,on_delete=models.CASCADE)
    success_rate = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Placed_student_Name = models.CharField(max_length=50, null=True)
    test_name = models.CharField(max_length=50, null=True)
    rank_scored=models.CharField(max_length=255)
    placed_year = models.PositiveBigIntegerField(validators=[
            MinValueValidator(1800), 
            MaxValueValidator(timezone.now().year)
        ], null=True)
    success_stories = models.TextField(blank=True, null=True)









class PGFacilitiesAndInfrastructure(models.Model):
    PG_facilities_id = models.PositiveIntegerField(primary_key=True)
    PG_institute = models.ForeignKey(PGInstitute, null=True,  on_delete=models.CASCADE)
    classroom_facilities = models.TextField(blank=True, null=True)
    lab_facilities = models.TextField(blank=True, null=True)
    library = models.TextField(blank=True, null=True)
    safety_and_security_measures = models.TextField(blank=True, null=True)

    def str(self):
        return self.classroom_facilities
    






class PGAdmissionProcess(models.Model):
    PG_admission_id = models.PositiveIntegerField(primary_key=True)
    PG_institute = models.ForeignKey(PGInstitute, null=True,  on_delete=models.CASCADE)
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

    #def str(self):
        #return self.PG_admission_id








class PGContactAndSupportForm(models.Model):
    PG_id = models.PositiveIntegerField(primary_key=True)
    PG_institute = models.ForeignKey(PGInstitute, null=True,  on_delete=models.CASCADE)
    PG_support_person = models.CharField(max_length=100) 
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







class PGAdditionalInformation(models.Model):
    PG_additional_id = models.PositiveIntegerField(primary_key=True)
    PG_institute = models.ForeignKey(PGInstitute, null=True,  on_delete=models.CASCADE)
    other_social_media_links = models.URLField(validators=[URLValidator()], blank=True, null=True)
    events_seminars = models.TextField(blank=True,null=True)
    news_updates = models.TextField(blank=True,null=True)

    #def str(self):
        #return self.PG_additional_id