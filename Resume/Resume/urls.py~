from django.conf.urls import patterns, include, url
from django.conf import settings 
from django.conf.urls.static import static
import django.contrib.auth.views
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),

    (r'^$',TemplateView.as_view(template_name='Contact_info.html')), 

    url(r'^UG_courses/$', 'Resume.views.UG_courses'),

    url(r'^PG_courses/$', 'Resume.views.PG_courses'),

    url(r'^Universities/$', 'Resume.views.Universities_list'),

    url(r'^UG_specialisations/$', 'Resume.views.UG_specialisations'),

    url(r'^PG_specialisations/$', 'Resume.views.PG_specialisations'), 

    url(r'^Email_info/$', 'Resume.views.Email_info'),

    url(r'^Education/$', 'Resume.views.Education'),

    url(r'^Projects/$', 'Resume.views.Projects'),

    url(r'^Personal/$', 'Resume.views.Personal'),


    
    url(r'^Contact_info/$', 'Resume.views.Contact_info'),

    url(r'^Education_info/$', 'Resume.views.Education_info'),

    url(r'^Personal_info/$', 'Resume.views.Personal_info'),

    url(r'^Projects_info/$', 'Resume.views.Projects_info'),

    url(r'^Resume_builder/$', 'Resume.views.Resume_builder'),

    url(r'^Contact_response/$',TemplateView.as_view(template_name='Education_info.html')), 

    url(r'^Education_response/$',TemplateView.as_view(template_name='Projects_info.html')),

    url(r'^Projects_response/$',TemplateView.as_view(template_name='Personal_info.html')),

)
