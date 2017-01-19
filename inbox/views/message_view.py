from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.utils import timezone

from base.views import AjaxableResponseMixin, SearchResponseMixin
from inbox.models import MessageManager, Message, Reply
from inbox.forms import ReplyForm
from authentication.models import User

class MessageListView(SearchResponseMixin, ListView):
	template_name = 'inbox/message/list.html'
	paginate_by = settings.PAGINATE_BY
	model = Message
	query = None

	def get_queryset(self):
		queryset = super(MessageListView, self).get_queryset()
		message_manager = MessageManager.objects.get_or_create(user=self.request.user)[0]
		if self.query == "receives":
			messages = queryset.filter(message_manager_receive=message_manager).exclude(message_manager_send=message_manager)
		elif self.query == "sends":
			messages = queryset.filter(message_manager_send=message_manager).exclude(message_manager_receive=message_manager)			
		elif self.query == "drafts":
			messages = queryset.filter(message_manager_receive=message_manager, message_manager_send=message_manager)
		else:
			messages = []
		return messages

	def get_context_data(self, ** kwargs):
		context = super(MessageListView, self).get_context_data(** kwargs)
		context['query'] = self.query
		context['message_manager'] = MessageManager.objects.get_or_create(user=self.request.user)[0]
		return context

class MessageCreateView(AjaxableResponseMixin, CreateView):
	template_name = 'inbox/message/form.html'
	model = Message
	fields = ['message_manager_receive','subject', 'text', 'file']

	def get_success_url(self):
		message_manager = MessageManager.objects.get_or_create(user=self.request.user)[0]
		if self.message.get_type(message_manager) == 'receives':
			return reverse_lazy('inbox:message_list_receives')
		elif self.message.get_type(message_manager) == 'sends':
			return reverse_lazy('inbox:message_list_sends')
		elif self.message.get_type(message_manager) == 'drafts':
			return reverse_lazy('inbox:message_list_drafts')
		else:
			return reverse_lazy('inbox:message_list_receives')

	def form_valid(self, form):
		self.message = form.save(commit=False)
		self.message.message_manager_send = MessageManager.objects.filter(user=self.request.user).first()
		
		from_email = self.message.message_manager_send.user.email
		to_email = self.message.message_manager_receive.user.email
		subject = self.message.subject
		text = self.message.text
		file = self.message.file
		
		if MessageSendView.send_message(from_email, to_email, subject, text, file):
			return HttpResponseRedirect(self.get_success_url())
		else:
			return 'ds'

	def get_context_data(self, ** kwargs):
		context = super(MessageCreateView, self).get_context_data(** kwargs)
		context['query'] = _("sends")
		return context

class MessageDetailView(SingleObjectMixin, FormMixin, ListView):
	template_name = 'inbox/message/detail.html'
	model = Reply
	form_class = ReplyForm

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Message.objects.all())
		if self.object.message_manager_receive.user == request.user:
			self.object.message_read = True
			self.object.save()
		return super(MessageDetailView, self).get(request, * args, ** kwargs)

	def get_context_data(self, ** kwargs):
		message_manager = MessageManager.objects.get_or_create(user=self.request.user)[0]
		context = super(MessageDetailView, self).get_context_data( ** kwargs)
		context['form'] = self.get_form()
		context['query'] =self.object.get_type(message_manager)
		return context

	def get_queryset(self):
		message = Message.objects.filter(slug=self.kwargs['slug']).first()
		replys = Reply.objects.filter(message=message)
		return replys

	def get_success_url(self):
		return reverse_lazy('inbox:message_detail', kwargs={'slug': self.kwargs['slug']})

	def post(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Message.objects.all())
		if self.object.message_manager_receive.user == request.user or self.object.message_manager_send.user == request.user:
			form = self.get_form()
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
			
	def form_valid(self, form):
		message = Message.objects.filter(slug=self.kwargs['slug']).first()
		message_manager = MessageManager.objects.get_or_create(user=self.request.user)[0]
		reply = form.save(commit=False)
		reply.message = message
		reply.message_manager = message_manager
		reply.save()
		message.last_modified = timezone.now()
		message.message_read = False
		message.save()
		return super(MessageDetailView, self).form_valid(form)


class MessageSendView():
	def send_message(from_email, to_email, subject, message, file=None):
		from_user = User.objects.filter(email=from_email).first()
		to_user = User.objects.filter(email=to_email).first()
		if not from_user or not to_user:
			return False
		from_message_manager = MessageManager.objects.filter(user=from_user).first()
		to_message_manager = MessageManager.objects.filter(user=to_user).first()
		if not from_message_manager or not to_message_manager:
			return False
		message = Message(
			message_manager_send=from_message_manager,
			message_manager_receive=to_message_manager,
			subject=subject,
			text=message,
			file=file
		)
		message.save()
		try:
			send_mail(subject, message, from_email, [to_email, ], fail_silently=False)
		except BadHeaderError:
			print "BadHeaderError"
		except Exception, e:
			print e
		return True

	send_message = staticmethod(send_message)
