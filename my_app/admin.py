from .models import Choice, Question, Member
from django.contrib import admin

# Register your models here.


admin.site.register(Question)
admin.site.register(Choice)
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Member, MemberAdmin)