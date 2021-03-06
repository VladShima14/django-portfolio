from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "published_date"]
    search_fields = ["title", "text"]


admin.site.register(Post, PostAdmin)