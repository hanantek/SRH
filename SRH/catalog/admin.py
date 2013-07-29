from django.contrib import admin, messages
from models import Nationality, DocumentType, Gender, CivilState

class NationalityAdmin(admin.ModelAdmin):
	pass

class DocumentTypeAdmin(admin.ModelAdmin):
	pass

class GenderAdmin(admin.ModelAdmin):
	pass

class CivilStateAdmin(admin.ModelAdmin):
	pass

class LevelEducationAdmin(admin.ModelAdmin):
	pass

class GradeAdmin(admin.ModelAdmin):
	pass

class IndustryAdmin(admin.ModelAdmin):
	pass

class LanguageAdmin(admin.ModelAdmin):
	pass

class LevelAdmin(admin.ModelAdmin):
	pass

admin.site.register(Nationality, NationalityAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(CivilState, CivilStateAdmin)