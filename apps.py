from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import os

class Config(object):
    namespace  = 'auctor'
    override   = 'AUCTOR'

    class directory(object):
        app   = os.path.dirname(os.path.realpath(__file__))
        cache = '%s/cache' % app

    class vn(object):
        name = _('Category name')
        categories = _('Sub categories')
        title = _('Title')
        content = _('Content')

    class ht(object):
        name = _('Name of the category')
        categories = _('Sub categories')
        title = _('Article title')
        content = _('Article content')

    class vbn(object):
        category = _('Category')
        article = _('Article')

    class vpn(object):
        category = _('Categories')
        article = _('Articles')

    class admin(object):
        log_fieldsets      = (_('Log informations'), {'fields': ('update_by', 'date_create', 'date_update', 'error', 'message')})
        category_fieldsets = (((None, { 'fields': ('name', 'categories'),})), (log_fieldsets))
        category_list_display    = ('name',)
        category_readonly_fields = ('update_by', 'date_create', 'date_update', 'error')
        category_filter_horizontal = ('categories',)
        article_fieldsets       =
        article_list_display    =
        article_readonly_fields =

if hasattr(settings, Config.override):
    for config,configs in getattr(settings, Config.override).items():
        if hasattr(Config, config):
            for key,value in configs.items():
                if hasattr(getattr(Config, config), key):
                    setattr(getattr(Config, config), key, value)


class AuctorConfig(AppConfig, Config):
    name = 'auctor'
