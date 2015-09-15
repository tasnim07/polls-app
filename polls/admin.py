from django.contrib import admin

# Register your models here.
from .models import Choice, Question

def make_published(modeladmin, request, queryset):
	queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	('Questions', {'fields': ['question_text', 'status']}),
	('Date information', {'fields':['pub_date'], 'classes': ['collapse'] }),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently', 'status',)
	list_filter = ['pub_date']
	search_fields = ['question_text']
	actions = [make_published]

	
admin.site.register(Question, QuestionAdmin)
