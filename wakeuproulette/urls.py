from django.conf.urls import patterns, include, url
from wakeup import views
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^alarm/', views.setAlarm, name='alarm'),
    url(r'start/', views.startRoulette, name='start'),

    # Serving Calls
    url(r'^conf/(?P<confname>.+)$', views.serveConference, name='conference'),
    url(r'^wakeuprequest/(?P<confname>.+)$', views.wakeUpRequest, name='wakeup'),
    url(r'^answercallback/(?P<confname>.+)$', views.answerCallback, name='answer-callback'),

#    url(r'newsletter/', views.newsletter, name='newsletter'),
    url(r'beta/', views.beta, name='beta'),

    url(r'survey/', views.survey, name='survey'),

    #    Handling responses
    url(r'callfeedback/(?P<conf>.+)$', views.processCallFeedback, name='callfeedback'),
    url(r'sms/', views.processSMS, name='sms'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns(''
    , url(r'^.*/', views.notFound, name='notFound')
)
