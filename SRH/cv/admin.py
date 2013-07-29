from django.contrib import admin, messages
from models import PersonalInfo

class PersonalInfoAdmin(admin.ModelAdmin):
	pass

admin.site.register(PersonalInfo, PersonalInfoAdmin)