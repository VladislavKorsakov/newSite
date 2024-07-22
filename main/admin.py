from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from main.models import User
from .models import Trustability

admin.site.register(User, UserAdmin)
admin.site.register(Trustability)


