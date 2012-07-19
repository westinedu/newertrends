from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.importlib import import_module
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.simple import direct_to_template

def main_page(request):
	template = get_template('main_page.html')
	variables = Context({
	  'head_title': 'Django Bookmarks',
	  'page_title': 'Welcome to Django Bookmarks',
	  'page_body': 'Where you can store and share bookmarks!'
	})
	output = template.render(variables)
	return HttpResponse(output)

def fb(request):
#	try:
#		user = User.objects.get(username=username)
#	except:
#		raise Http404('Requested user not found.')
#	bookmarks = user.bookmark_set.all()
  
	#return render_to_response('registration/blank.html')
    return direct_to_template(request, 'registration/fblogin.html')

def image(request):
    image_data = open("static/images/logo.png", "rb").read()
    return HttpResponse(image_data,mimetype="image/png")

def html5(request):
    return render_to_response('html5/html5example.html')