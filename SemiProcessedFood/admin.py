from django.contrib import admin
from SemiProcessedFood.models import *
from django.utils.html import linebreaks
from django.utils.html import format_html

class Categorydmin(admin.ModelAdmin):
    fieldsets = [
        ('产品分类', {'fields': ['name']})
    ]
    list_display = ['name']
admin.site.register(Category, Categorydmin)

class Fooddmin(admin.ModelAdmin):
    fieldsets = [
        ('食品配置', {'fields': ['name', 'category', 'description', 'active']}),
        ('图片', {'fields': ['image_location']})
    ]
    list_display = ['name', 'category', 'image', 'description_linebreak', 'active']
    search_fields = ['name']

    def description_linebreak(self, obj):
        return format_html(linebreaks(obj.description))
    description_linebreak.short_description = '描述'
    description_linebreak.allow_tags = True



admin.site.register(Food, Fooddmin)