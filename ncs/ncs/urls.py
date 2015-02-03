from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ncs.views.home', name='home'),
    url(r'mark', 'ncs.views.attendance', name='attendance'),
    # url(r'stats', 'ncs.views.stats', name='stats'),
    # url(r'profile', 'ncs.views.profile', name='profile'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
