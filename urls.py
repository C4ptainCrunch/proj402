# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from utils.decorators import AR
from utils.authentification import intra_auth
from settings import VERSION

def home(request):
    if request.user.is_authenticated():
        return redirect('profile')
    return render(request, "layout.tpl")

urlpatterns = patterns('',
    url(r'^user/', include('users.urls'), name='users'),
    url(r'^category/', include('categories.urls'), name='categories'),
    url(r'^course/', include('courses.urls'), name='courses'),
    url(r'^document/', include('documents.urls'), name='documents'),
    url(r'^msg/', include('messages.urls'), name='messages'),
    url(r'^notification/', include('notifications.urls'), name='notifications'),
    url(r'^admin/', include('admin.urls'), name='admin'),
    url(r'^vote/', include('upvotes.urls'), name='votes'),
    url(r'^search/', include('search.urls'), name='search'),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^$', home, name='index'),

    (r'^favicon\.ico$', 
     'django.views.generic.simple.redirect_to', 
     {'url': '/static/favicon.ico'}),

    # entry point
    url(r'^zoidberg$', login_required(direct_to_template),
        {'template': 'base.tpl'}, name='z-index'),

    url('^help$', 
        AR(direct_to_template), 
        {'template': 'help.tpl',
         'extra_context': {'VERSION' : VERSION}},
        name='help'),

    url(r'^auth$', intra_auth, name="auth"),
)
