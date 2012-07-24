from django.conf.urls.defaults import *
from mezzanine.core.views import direct_to_template
from bookmarks.views import *
from django.contrib import admin
from zinnia.urls import *
from django.contrib.comments.urls import *
admin.autodiscover()
handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',    
    url(r"^$", direct_to_template, {"template": "index.html"}, name="home"),
    (r'^admin/', include(admin.site.urls)),
 #   (r'^accounts/', include('registration.backends.default.urls')),
    (r'image', image),
    (r'html5', html5),
    (r'^djangobook/','django.views.generic.simple.direct_to_template',
     {'template': 'djangobook/The Django Book  Version 2.0 (English).htm'}),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^home$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
    ('^evertodo$', 'django.views.generic.simple.redirect_to',
     {'url': '/evertodo/'}),
    (r'^weblog/', include('zinnia.urls')),
    (r'^comments/', 'django.contrib.comments.urls'),
)

