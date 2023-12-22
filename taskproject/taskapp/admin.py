from django.contrib import admin

from .models import Task, ChecklistItem


class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type", "due")
    list_display_links = ("title",)


class ChecklistItemAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "checked")
    list_display_links = ("content",)


admin.site.register(Task, TaskAdmin)
admin.site.register(ChecklistItem, ChecklistItemAdmin)
