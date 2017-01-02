from django.contrib import admin

from submission.models import (Event, Submission, Review)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	pass

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
	pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	pass
