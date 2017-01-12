from django.forms import ModelForm
from inbox.models import Reply

class ReplyForm(ModelForm):
	class Meta:
		model = Reply
		fields = ("text", "file")