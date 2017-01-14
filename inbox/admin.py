from django.contrib import admin

from inbox.models import (MessageManager, Message, Reply)

@admin.register(MessageManager)
class MessageManagerAdmin(admin.ModelAdmin):
	pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	pass

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
	pass
