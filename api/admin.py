from django.contrib import admin

from api.models import Task, Category

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_completed', 'created_at', 'category')

admin.site.register(Category)