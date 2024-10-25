from django.contrib import admin
from .models import Question
from .models import Answer

#class로 데이터를 검색하기
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# Question을 불러온다.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)