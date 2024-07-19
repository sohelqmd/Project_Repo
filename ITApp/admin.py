from django.contrib import admin
from .models import ItInstitute,ItContactInformation,ItLocationInformation,\
It_Course_Chocies,ItCourseForm,ItPlacementDetails,ItTrainer,\
ItFacilitiesAndInfrastructure,ItAdmissionProcess,ItContactAndSupportForm,\
ItAdditionalInformation

class ItInstituteAdmin(admin.ModelAdmin):
  list_display=['It_id','it_institute_name','summary',
  'established_year','website_url','accreditation_details',
  'mission','vision','affiliations','achievements_and_awards']

class ItContactInformationAdmin(admin.ModelAdmin):
  list_display=['it_contact_id','it_institute','it_contact_person', 
  'phone_number', 'email_address', 'office_hour_start', 
  'office_hour_end', 'social_media_links']

class ItLocationInformationAdmin(admin.ModelAdmin):
    list_display = ['it_location_id', 'it_institute', 'address', 
                  'city', 'state', 'pin_code', 'nearby_landmarks']
    
class ItCourseChoicesAdmin(admin.ModelAdmin):
   list_display = ['it_course_no','it_course_name']

class ItCourseFormAdmin(admin.ModelAdmin):
   list_display = ['it_course_id', 'it_institute', 'it_courses', 
    'duration_days', 'duration', 'fee_range', 'class_timing_start', 
    'class_timing_end', 'batch_size', 'batch_start_date', 
    'demo_classes_available', 'demo_date', 'certification_details', 
    'mode_of_instruction', 'language_of_instruction']
   
class ItTrainerAdmin(admin.ModelAdmin):
    list_display = ['It_trainer_id', 'it_institute', 'it_courses', 
    'it_trainer_name', 'qualifications', 'experience_years', 
    'specializations', 'achievements']

class ItPlacementDetailsAdmin(admin.ModelAdmin):
    list_display = ['It_Placement_id', 'it_institute', 
    'placement_statistics', 'placement_count', 'companies_associated', 
    'placement_process', 'mock_interview', 'mock_test', 'softskills',
    'success_stories', 'internship_opportunities']

class ItFacilitiesAndInfrastructureAdmin(admin.ModelAdmin):
    list_display = ['it_facilities_id', 'it_institute', 
    'classroom_facilities', 'lab_facilities', 'library', 
    'safety_and_security_measures']

class ItAdmissionProcessAdmin(admin.ModelAdmin):
    list_display = ['it_admission_id', 'it_institute', 
    'admission_requirements', 'application_process', 
    'application_start', 'application_deadline', 
    'exam_date', 'admission_fee', 'scholarships', 
    'entrance_exams_accepted', 'interview_process']

class ItAdditionalInformationAdmin(admin.ModelAdmin):
    list_display = ['it_additional_id', 'it_institute', 
    'other_social_media_links', 'events_seminars', 'news_updates']

# Register your models here.
#IIAPP admin 
admin.site.register(ItInstitute, ItInstituteAdmin)
admin.site.register(ItContactInformation, ItContactInformationAdmin)
admin.site.register(ItLocationInformation, ItLocationInformationAdmin)
admin.site.register(It_Course_Chocies, ItCourseChoicesAdmin)
admin.site.register(ItCourseForm, ItCourseFormAdmin)
admin.site.register(ItTrainer, ItTrainerAdmin)
admin.site.register(ItPlacementDetails, ItPlacementDetailsAdmin)
admin.site.register(ItFacilitiesAndInfrastructure, ItFacilitiesAndInfrastructureAdmin)
admin.site.register(ItAdmissionProcess, ItAdmissionProcessAdmin)
admin.site.register(ItContactAndSupportForm)
admin.site.register(ItAdditionalInformation,ItAdditionalInformationAdmin)


