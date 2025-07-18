from django.contrib import admin

from apps.accounts.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'avatar')
    search_fields = ('username', 'email', 'role')
    filter_horizontal = ('groups', 'user_permissions')
    fieldsets = (
        ('Personal Info', {'fields': ('username', 'email', 'role', 'avatar')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
    )
    list_filter = ('role',)
    
admin.site.register(CustomUser, CustomUserAdmin)
