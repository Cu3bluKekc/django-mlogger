# -*- coding: utf-8 -*-
# (c) 2009-2010 Ruslan Popov <ruslan.popov@gmail.com>
# (c) 2010 Maxim M. <shamanu4@gmail.com>

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from mlogger.models import Log


class AdminLog(admin.ModelAdmin):
    list_display = ('user', 'action', 'content_type', 'timestamp')
    readonly_fields = ('user', 'action', '_object', 'data', 'timestamp')
    exclude = ('content_type', 'oid', )

    def _object(self, object):
        app_label = object.content_type.app_label
        model = object.content_type.model
        oid = object.oid
        text = u'{app_label}.{model}:{oid}'.format(app_label=app_label,
                                                   model=model,
                                                   oid=oid)
        url = u'#'
        if object.action in ('create', 'update'):
            try:
                url = reverse('admin:{app_label}_{model}_change'.\
                        format(app_label=app_label,
                               model=model), args=[oid])
            except:
                pass
        return u'<a href="{url}">{text}</a>'.format(url=url, text=text)
    _object.allow_tags = True
    _object.short_description = _('object')
    
admin.site.register(Log, AdminLog)
Log.description = _(u'This model consists of all meaningful events of system.')
