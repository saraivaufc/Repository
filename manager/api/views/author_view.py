from django.http import Http404
from django.core.exceptions import PermissionDenied

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from manager.api.serializers import  AuthorSerializer, AuthorSerializerPk

from manager.models import Author

class AuthorAPIView(APIView):

	def get(self, request, pk=None, format=None):
		if pk:
			author = Author.objects.get(pk=pk)
			serializer = AuthorSerializer(author, context={'request': request}, many=False)
		else:
			authors = Author.objects.all()
			serializer = AuthorSerializerPk(authors, context={'request': request}, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		if not request.user.has_perm('manager.add_author'):
			raise PermissionDenied

		serializer = AuthorSerializer(data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		if not request.user.has_perm('manager.delete_author'):
			raise PermissionDenied
			
		author = self.get_object(pk)
		author.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)