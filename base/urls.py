from django.conf.urls import patterns, include, url

from . import views
urlpatterns = patterns('base.views',
    url(r'^$', 'home', name='home'),

	url(r'^events/$', views.IndexView.as_view(), name = 'events'),

	# events/5/
	url(r'^events/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'event_detail'),
)