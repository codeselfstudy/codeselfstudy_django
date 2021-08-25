from django.contrib import admin

from .models import Quiz, Question, Choice


class QuizAdmin(admin.ModelAdmin):
    list_display = ("title",)
    # list_display = ()
    # readonly_fields = ()
    # fieldsets = []


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Choice)
