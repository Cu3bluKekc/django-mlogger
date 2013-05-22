# -*- coding: utf-8 -*-
# (c) 2009-2010 Ruslan Popov <ruslan.popov@gmail.com>
# (c) 2010 Maxim M. <shamanu4@gmail.com>

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from json import loads
from mlogger.models import Log
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse


class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'content_type', 'timestamp')
    readonly_fields = ('user', 'action', '_object', '_data', 'timestamp')
    exclude = ('content_type', 'data', 'oid', )

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

    def _data(self, object):
        data = loads(object.data).items()
        return mark_safe('<ul>%s</ul>' % ''.\
                         join(['<li>%s: %s</li>' % (k, v, ) for k, v in data]))
    _data.allow_tags = True
    _data.short_description = _('Data')

admin.site.register(Log, LogAdmin)
Log.description = _(u'This model consists of all meaningful events of system.')
