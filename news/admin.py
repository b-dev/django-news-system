'''
Created on Oct 9, 2009

@author: grokrz
'''
from django.contrib import admin
from news.models import News
from news.forms import NewsAdminModelForm

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title','user', 'created_at', 'published')
    search_fields = ['body', 'title']
    ordering = ('-created_at',)
    list_filter = ('created_at', 'updated_at', 'published')
    
    fieldsets = [
        ('General', {'fields': ['user', 'title', 'slug'],}),
        ('', {'fields': ['body']}),
        ('Published', {'fields': ['published']}),
    ]
    form = NewsAdminModelForm


admin.site.register(News, NewsAdmin)