from django.contrib import admin
from LoginApp.models import UserProfileInfo, User ,Gender ,Company

admin.site.register(UserProfileInfo)
admin.site.register(Gender)
admin.site.register(Company)