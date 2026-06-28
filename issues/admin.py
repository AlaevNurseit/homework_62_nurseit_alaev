from django.contrib import admin
from .models import Issue, Status,Type


class IssueAdmin(admin.ModelAdmin):
    list_display = ['summary', 'description', 'status',]
    list_filter = ['status']
    search_fields = ['description']


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)

