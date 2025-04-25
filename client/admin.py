from django.contrib import admin
from .models import HealthProgram, Client, Enrollment


@admin.register(HealthProgram)
class HealthProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'date_of_birth', 'contact_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'contact_number')
    list_filter = ('gender', 'created_at')
    
    def full_name(self, obj):
        return obj.full_name


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'program', 'enrollment_date', 'notes')
    search_fields = ('client__first_name', 'client__last_name', 'program__name')
    list_filter = ('enrollment_date',)

