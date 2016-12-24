from django.contrib import admin

from manager.models import (Author, Collection, Community, Keyword, 
	Publication, Subject, Publisher)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
	pass

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
	pass

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
	pass

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
	pass

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
	pass