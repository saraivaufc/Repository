class HierarchyResponseMixin(object):
	"""
	hierarchy_fields must contains list with name field(name), type of id(id), id(slug or pk) and model.
	Example:  

	import Author
	hierarchy_fields= [
		{'name':'author', 'id': 'pk', 'pk':'author_pk', 'model': Author},
	]
	"""
	hierarchy_fields = {}

	def get_queryset(self):
		queryset = super(HierarchyResponseMixin, self).get_queryset()
		kwargs = {}
		for field in self.hierarchy_fields:
			kwargs[field['name']] = field['model'].objects.filter(** {field['id']:self.kwargs[field[field['id']]]})
		return queryset.filter(**kwargs)

	def get_context_data(self, ** kwargs):
		context = super(HierarchyResponseMixin, self).get_context_data( ** kwargs)
		for field in self.hierarchy_fields:
			context[field['name']] = field['model'].objects.filter(** {field['id']:self.kwargs[field[field['id']]]}).first()
		return context