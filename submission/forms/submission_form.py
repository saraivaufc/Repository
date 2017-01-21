# -*- encoding=utf-8 -*-

from django.forms import ModelForm
from submission.models import Submission


class SubmissionForm(ModelForm):
	def __init__(self, event, *args, **kwargs):
		super(SubmissionForm, self).__init__(*args, **kwargs)
		self.fields['subjects'].queryset = event.subjects.all()
		self.fields['community'].queryset = event.communities.all()
		self.fields['collection'].queryset = event.collections.all()
		self.fields['publisher'].queryset = event.publishers.all()

	class Meta:
		model = Submission
		fields = ('title', 'typology', 'authors', 'subjects', 'community', 'collection', 'publisher', 'reference','principal_language', 'principal_abstract', 'principal_keywords', 'secondary_language', 'secondary_abstract', 'secondary_keywords', 'file')