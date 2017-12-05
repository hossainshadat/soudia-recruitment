from django.contrib import admin

# Register your models here.

from .models import Employer, Candidate, We_work

admin.site.register(Employer)
admin.site.register(Candidate)
admin.site.register(We_work)