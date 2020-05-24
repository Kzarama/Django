from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import Profile

@admin.register(Profile)
class ProfileAdmon(admin.ModelAdmin):
    # display field in the superadmin interface
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # links to display information
    list_display_links = ('pk', 'user')
    # list the fields to edit
    list_editable = ('phone_number', 'website', 'picture')
    # fields to search
    search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name', 'phone_number')
    # filter users
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')
    # fields to edit
    fieldsets = (
        # (None, {
        ('Profile', {
            # 'fields':(('user', 'picture'),),
            'fields':('user', 'picture'),
        }),

        ('Metadata',{
            'fields':(('created', 'modified'),),
        }),
    )
    # fields only read
    readonly_fields = ('created', 'modified')

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)