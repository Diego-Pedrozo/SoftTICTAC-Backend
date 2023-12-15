from django.contrib import admin
from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from apps.estadisticas.models.stats import UserStatsModel#

class UserInformationInline(admin.StackedInline):
    model = UserInformationModel
    can_delete = False

class UserStatsInline(admin.StackedInline):
    model = UserStatsModel
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    #list_display = ('username', 'email', 'first_name', 'last_login', 'date_joined')
    list_display = ('id', 'username', 'first_name', 'last_name', 'get_user_role')
    inlines = [UserInformationInline, UserStatsInline]
    search_fields = ['username', 'email', 'first_name', 'last_name']

    def get_user_role(self, obj):
        user_info = UserInformationModel.objects.get(user=obj)
        return user_info.get_user_type_display() if user_info else "N/A"

    get_user_role.short_description = 'User Role'


admin.site.unregister(User)

admin.site.register(User, UserAdmin)
