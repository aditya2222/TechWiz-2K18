from django.contrib import admin
from blog.models import Post,Comment,Rule,Event,Registration
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_date','published_date')

class RuleAdmin(admin.ModelAdmin):
    list_display = ('title','created_date','published_date')

class RegsitrationAdmin(admin.ModelAdmin):
    list_display = ('firstName','event','rollNumber','paynow')



admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Rule,RuleAdmin)
admin.site.register(Event)
admin.site.register(Registration,RegsitrationAdmin)

