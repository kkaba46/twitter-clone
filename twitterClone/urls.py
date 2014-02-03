from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitterClone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^twitter/index$','twitter.views.index'),
    url(r'^twitter/login$','twitter.views.login'),
    url(r'^twitter/logout$','twitter.views.logout'),
    url(r'^twitter/signup$','twitter.views.signup'),
    url(r'^admin/', include(admin.site.urls)),
)
