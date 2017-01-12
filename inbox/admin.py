from django.contrib import admin

from inbox.models import (ChatManager, Chat, Reply)

@admin.register(ChatManager)
class ChatManagerAdmin(admin.ModelAdmin):
	pass

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
	pass

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
	pass
