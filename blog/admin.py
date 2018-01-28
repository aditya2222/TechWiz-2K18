from django.contrib import admin
from blog.models import Post,Comment,Rule,Event
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_date','published_date')

class RuleAdmin(admin.ModelAdmin):
    list_display = ('title','created_date','published_date')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Rule,RuleAdmin)
admin.site.register(Event)

