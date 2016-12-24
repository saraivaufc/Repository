import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from django.db.models import signals
from django.db.models.signals import post_save

group_permissions = {
	"default": [
		#community
	],
	"admin": [
		#community
		"add_community",
		"change_community",
		"delete_community",
		#author
		"add_author",
		"change_author",
		"delete_author",
		#collection
		"add_collection",
		"change_collection",
		"delete_collection",
		#keyword
		"add_keyword",
		"change_keyword",
		"delete_keyword",
		#publication
		"add_publication",
		"change_publication",
		"delete_publication",
		#publisher
		"add_publisher",
		"change_publisher",
		"delete_publisher",
		#subject
		"add_subject",
		"change_subject",
		"delete_subject",
	]
}

def create_user_groups(app, created_models, verbosity, **kwargs):
	if verbosity > 0:
		print "Initialising data post_syncdb"

	for group in group_permissions:
		model = User
		content_type = ContentType.objects.get_for_model(model)
		role, created = Group.objects.get_or_create(name=group)
		if verbosity > 1 and created:
			print 'Creating group', group
		for perm in group_permissions[group]:
			perm = Permission.objects.get(codename=perm)
			role.permissions.add(perm)
			if verbosity > 1:
				print 'Permitting', group, 'to', perm
		role.save()


def default_group(sender, instance, created, **kwargs):
	if created:
		instance.groups.add(Group.objects.get(name='default'))


post_save.connect(default_group, sender=User)

signals.post_syncdb.connect(
	create_user_groups,
	sender=models,
	dispatch_uid='manager.models.create_user_groups'
)
