from django.conf.urls import patterns, include, url


from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    url(r'^what-it-does/$', 'signups.views.whatitdoes', name='whatitdoes'),
    url(r'^ce-qu-il-fait/$', 'signups.views.cequilfait', name='cequilfait'),
    url(r'^used-programmes/$', 'signups.views.usedprogrammes', name='usedprogrammes'),    
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
