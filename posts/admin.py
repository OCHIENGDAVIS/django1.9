from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'timestamp', 'updated', 'title']
    list_display_links = ['updated', 'title']
    list_filter = ['timestamp', 'updated']
    search_fields = ['title', 'content']
    class Meta:
        model = Post


admin.site.register(Post,PostAdmin)
