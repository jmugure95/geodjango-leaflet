from django.contrib import admin
from .models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','slug','body','date',) 
	prepopulated_fields = {'slug':('title',)}


admin.site.register(Article, ArticleAdmin)