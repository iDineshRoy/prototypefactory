from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
# from django.contrib.auth import get_user_model as User
from accounts.models import User

INDUSTRY_CHOICES = (
    ('Accounting', 'Accounting'),
    ('Administration & Office Support','Administration & Office Support'),
    ('Advertising, Arts & Media', 'Advertising, Arts & Media'),
    ('Banking & Financial Services', 'Banking & Financial Services'),
    ('Call Centre & Customer Service', 'Call Centre & Customer Service'),
    ('CEO & General Management', 'CEO & General Management'),
    ('Community Services & Development', 'Community Services & Development'),
    ('Construction', 'Construction'),
    ('Consulting & Strategy', 'Consulting & Strategy'),
    ('Design & Architecture', 'Design & Architecture'),
    ('Education & Training', 'Education & Training'),
    ('Engineering', 'Engineering'),
    ('Farming, Animals & Conservation', 'Farming, Animals & Conservation'),
    ('Government & Defence', 'Government & Defence'),
    ('Healthcare & Medical', 'Healthcare & Medical'),    
    ('Hospitality & Tourism', 'Hospitality & Tourism'),
    ('Human Resources & Recruitment', 'Human Resources & Recruitment'),
    ('Information & Communication Technology', 'Information & Communication Technology'),
    ('Insurance & Superannuation', 'Insurance & Superannuation'),
    ('Legal', 'Legal'),
    ('Manufacturing, Transport & Logistics', 'Manufacturing, Transport & Logistics'),
    ('Marketing & Communications', 'Marketing & Communications'),
    ('Mining, Resources & Energy', 'Mining, Resources & Energy'),
    ('Real Estate & Property', 'Real Estate & Property'),
    ('Retail & Consumer Products', 'Retail & Consumer Products'),
    ('Sales', 'Sales'),
    ('Science & Technology', 'Science & Technology'),
    ('Self Employment', 'Self Employment'),
    ('Sport & Recreation', 'Sport & Recreation'),
    ('Trades & Services', 'Trades & Services'),
)

STATE_CHOICES = (
    ('New South Wales', 'New South Wales'),
    ('Victoria', 'Victoria'), 
    ('Queensland', 'Queensland'), 
    ('South Australia', 'South Australia'), 
    ('Western Australia', 'Western Australia'),
    ('Tasmania', 'Tasmania'),
    ('Northern Territory', 'Northern Territory'),
    ('Australian Capital Territory', 'Australian Capital Territory'),
)

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = RichTextField()
    technology = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=50, null=True, default="open")
    location = models.CharField(max_length=50, null=True, choices=STATE_CHOICES)
    industry = models.CharField(max_length=50, null=True, choices=INDUSTRY_CHOICES)
    company = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    interests = models.ManyToManyField(User, related_name="interests")