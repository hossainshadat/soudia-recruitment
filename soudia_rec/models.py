from django.db import models

# Create your models here.

CATAGORY = (
    ('PART TIME', 'Part Time'),
    ('FULL TIME', 'Full Time'),
    ('URGENT', 'Urgent'),
)


class Employer(models.Model):
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='employe', blank=True, null=True)
    city =	models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    content_max_20_words = models.TextField()
    job_type = models.CharField(max_length=100, choices=CATAGORY)

    def __str__(self):
        return self.designation

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='candidate', blank=True, null=True)
    city =	models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    content_max_20_words = models.TextField()

    def __str__(self):
        return self.name

class We_work(models.Model):
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company', blank=True, null=True)

    def __str__(self):
        return self.company_name




