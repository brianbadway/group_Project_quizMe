from django.contrib import admin

from .models import Question, Quiz, Answer

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Answer)

# Register your models here.
