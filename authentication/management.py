from authentication.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

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
		#su, inbmission
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

def create_user_groups(sender, **kwargs):
	print "Initialising data post_migrate"

	for group in group_permissions:
		model = User
		content_type = ContentType.objects.get_for_model(model)
		role, created = Group.objects.get_or_create(name=group)
		for perm in group_permissions[group]:
			try:
				perm = Permission.objects.get(codename=perm)
			except Exception, e:
				print e, ">>" ,perm
				continue
			role.permissions.add(perm)
		role.save()