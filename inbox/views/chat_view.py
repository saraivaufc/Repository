from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from base.views import AjaxableResponseMixin
from inbox.models import ChatManager, Chat, Reply
from inbox.forms import ReplyForm

class ChatListView(ListView):
	template_name = 'inbox/chat/list.html'
	paginate_by = settings.PAGINATE_BY
	model = Chat

	def get_queryset(self):
		chat_manager = ChatManager.objects.get_or_create(user=self.request.user)[0]
		chats = None
		replys = self.request.GET.get('query')
		if replys and (replys == 'send'):
			chats = Chat.objects.filter(chat_manager_send=chat_manager)
		elif replys and (replys == 'receive'):
			chats = Chat.objects.filter(chat_manager_receive=chat_manager)
		else:
			chats_send = Chat.objects.filter(chat_manager_send=chat_manager)
			chats_receive = Chat.objects.filter(chat_manager_receive=chat_manager)
			chats = list(chats_send) + list(chats_receive)
		return chats

	def get_context_data(self, ** kwargs):
		context = super(ChatListView, self).get_context_data(** kwargs)
		context['query'] = self.request.GET.get('query')
		return context

class ChatCreateView(AjaxableResponseMixin, CreateView):
	template_name = 'inbox/chat/form.html'
	model = Chat
	fields = ['chat_manager_receive','subject', 'text', 'file']
	success_url = reverse_lazy('inbox:chat_list')

	def form_valid(self, form):
		chat=form.save(commit=False)
		chat.chat_manager_send = ChatManager.objects.get_or_create(user=self.request.user)[0]
		chat.save()
		return super(ChatCreateView, self).form_valid(form)

class ChatDetailView(SingleObjectMixin, FormMixin, ListView):
	template_name = 'inbox/chat/detail.html'
	model = Reply
	form_class = ReplyForm

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Chat.objects.all())
		return super(ChatDetailView, self).get(request, * args, ** kwargs)

	def get_context_data(self, ** kwargs):
		context = super(ChatDetailView, self).get_context_data( ** kwargs)
		context['current'] = 'all'
		context['form'] = self.get_form()
		return context

	def get_queryset(self):
		chat = Chat.objects.filter(slug=self.kwargs['slug']).first()
		replys = Reply.objects.filter(chat=chat)
		return replys

	def get_success_url(self):
		return reverse_lazy('inbox:chat_detail', kwargs={'slug': self.kwargs['slug']})

	def post(self, request, * args, ** kwargs):
		if not request.user.is_authenticated():
			return HttpResponseForbidden()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
	def form_valid(self, form):
		chat = Chat.objects.filter(slug=self.kwargs['slug']).first()
		chat_manager = ChatManager.objects.get_or_create(user=self.request.user)[0]
		reply = form.save(commit=False)
		reply.chat = chat
		reply.chat_manager = chat_manager
		reply.save()
		return super(ChatDetailView, self).form_valid(form)
