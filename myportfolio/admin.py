from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Person)
admin.site.register(Email)
admin.site.register(SocialContact)
admin.site.register(WorkDuration)
admin.site.register(Work)
admin.site.register(FrontendSkill)
admin.site.register(BackendSkill)
admin.site.register(ProgrammingLanguage)
admin.site.register(ContactUs)
