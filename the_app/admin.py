from django.contrib import admin
from .models import news,product
# Register your models here.

class newsadmin(admin.ModelAdmin):
    list_display = ('DateTime','title','auther','body')
    list_filter = ('DateTime','title','auther')
    search_fields = ('title','auther')
    list_per_page = 10
    ordering = ('DateTime',)

admin.site.register(news,newsadmin)
admin.site.register(product)