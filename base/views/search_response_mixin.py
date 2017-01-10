
class SearchResponseMixin(object):

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.model.get_search_fields()):
			kwargs = {("%s__contains" % (query,)):text}
			return self.model.objects.filter(** kwargs)
		else:
			return self.model.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(SearchResponseMixin, self).get_context_data( ** kwargs)
		context["model"] = self.model
		return context