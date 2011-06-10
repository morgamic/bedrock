from django.conf.urls.defaults import patterns


urlpatterns = patterns('',
    # Example:
    (r'^careers/?$', 'careers.views.careers'),
    (r'^careers/all/?$', 'careers.views.careers_two'),
    (r'^careers/(?P<slug>[\w-]+)/$', 'careers.views.department'),
    (r'^careers/position/(?P<job_id>[\w]+)/$', 'careers.views.position'),
    (r'^careers/benefits/?$', 'careers.views.benefits'),
)