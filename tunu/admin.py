from django.contrib import admin
from .models import Contact

# Register the Contact model with custom admin settings (optional)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')  # Fields to display in the admin list view
    search_fields = ('name', 'email', 'subject')  # Fields to include in the search bar
    list_filter = ('created_at',)  # Filters in the admin sidebar
    ordering = ('-created_at',)  # Default ordering (newest first)
