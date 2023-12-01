from django.contrib import admin
from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel

class UserInformationInline(admin.StackedInline):
    model = UserInformationModel
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    #list_display = ('username', 'email', 'first_name', 'last_login', 'date_joined')
    list_display = ('username', 'first_name', 'last_name')
    inlines = [UserInformationInline]
    search_fields = ['username', 'email', 'first_name', 'last_name']


admin.site.unregister(User)

admin.site.register(User, UserAdmin)
