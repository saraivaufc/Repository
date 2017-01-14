import models
from authentication.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.db.models import signals
from django.db.models.signals import post_save

group_permissions = {
	"participant": [
		#author
		"add_author",
		#keyword
		"add_keyword",
		#submission
		"add_submission",
		"change_submission",
		"delete_submission",
		#message
		"add_message",
		"change_message",
		"delete_message",
		#reply
		"add_reply",
		"change_reply",
		"delete_reply",
	],
	"reviser": [
		#submission
		"list_submission_to_review",

		"add_review",
		"change_review",
		"delete_review",
	],
	"administrator": [
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
		#event
		"add_event",
		"change_event",
		"delete_event",
		#submission
		"list_submission_to_review",
		"submit_final",
		#Reviser
		"list_reviser",
		"add_reviser",
		"change_reviser",
		"delete_reviser",
		#Administrator
		"list_administrator",
		"add_administrator",
		"delete_administrator",
		#Participant
		"list_participant",
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
			try:
				perm = Permission.objects.get(codename=perm)
			except Exception, e:
				print e, ">>" ,perm
				continue
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
	dispatch_uid='authentication.models.create_user_groups'
)
