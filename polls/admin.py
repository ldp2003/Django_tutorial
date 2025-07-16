from django.contrib import admin
from .models import Question, Choice

# Register your models here.
#model phải register ở admin trước
admin.site.register(Question)

#Có thể truyền vào argument thứ 2 để define cách hiển thị trong table (cách 2)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ( 'choice_text', 'votes',)

admin.site.register(Choice, ChoiceAdmin)
