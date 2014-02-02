from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitterClone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^twitter/static_file$','twitter.views.static_file'),
    url(r'^admin/', include(admin.site.urls)),
)
