from django.shortcuts import render

from manager.models import Community
from public import *
from admin import *

def home(request):
	if request.user.has_perm('manager.access_admin_site'):
		return render(request, 'manager/admin/index.html', {'request': request})
	else:
		return render(request, 'manager/public/index.html', {'request': request})