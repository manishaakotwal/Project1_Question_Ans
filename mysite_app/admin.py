from django.contrib import admin

# Register your models here.
from . models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ("question_text", "pub_date")
    
# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ("choice_text", "votes")    
    