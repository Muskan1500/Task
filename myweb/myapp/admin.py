from django.contrib import admin

# Register your models here.
from .models import UserProfile, ContactSubmission

admin.site.register(UserProfile)
admin.site.register(ContactSubmission)