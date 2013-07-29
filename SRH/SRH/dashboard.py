#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

class CustomIndexDashboard(Dashboard):
    def __init__(self, **kwargs):
            Dashboard.__init__(self, **kwargs)
            self.children.append(modules.Group(
                title= _('Admin central'),
                column=1,
                collapsible=True,
                children=[
                    modules.AppList(
                        title=_('Administration'),
                        collapsible=False,
                        models=('django.contrib.*',)
                    ),
                    modules.AppList(
                        title=_('Applications'),
                        collapsible=False,
                        exclude=('django.contrib.*',)
                    )
                ]
            ))
            
            self.children.append(modules.AppList(
                title=_('Admin'),
                column=1,
                collapsible=True,
                models=('django.contrib.*',)
            ))
            
            self.children.append(modules.AppList(
                title=_('Apps'),
                column=1,
                collapsible=True,
                exclude=('django.contrib.*',)
            ))
            
            self.children.append(modules.RecentActions(
                title=_('Recent Actions'),
                column=3,
                collapsible=False,
                limit=5,
            ))