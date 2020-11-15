from django.contrib import admin
from blogapi.models import Post

# Register your models here.


# admin.site.register(Post, admin.ModelAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'status', 'publish_date', 'update_date')

admin.site.register(Post, PostAdmin)
