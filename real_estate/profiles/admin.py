from django.contrib import admin
from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "pkid", "user", "gender", "phone_number", "country", "city")
    list_filter = ("gender", "country", "city")
    list_display_links = ("id", "pkid", "user")


admin.site.register(Profile, ProfileAdmin)
