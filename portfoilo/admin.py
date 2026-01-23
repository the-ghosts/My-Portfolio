from django.contrib import admin
from .models import MyProject, ContactMessage

@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'sent_at')

# Register your models here.
