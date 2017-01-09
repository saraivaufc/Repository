from rest_framework import serializers

from manager.models import Author

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Author
		fields = ('id', 'slug','first_name', 'last_name', 'reference_name',)

class AuthorSerializerPk(AuthorSerializer):
	class Meta(AuthorSerializer.Meta):
		fields = ('id', 'slug',)