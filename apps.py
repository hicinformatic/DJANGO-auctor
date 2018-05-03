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
        author = _('Author')
        language = _('Language')
        description = _('Description')

    class ht(object):
        name = _('Name of the category')
        categories = _('Sub categories')
        title = _('Article title')
        content = _('Article content')
        author = _('Article author')
        language = _('Language')
        description = _('Description')
        list_html_br = _('Articles')

    class vbn(object):
        category = _('Category')
        article = _('Article')
        language = _('Language')

    class vpn(object):
        category = _('Categories')
        article = _('Articles')
        language = _('Languages')

    class default(object):
        language = 'en'

    class admin(object):
        log_fieldsets              = (_('Log informations'), {'fields': ('update_by', 'date_create', 'date_update', 'error', 'message')})
        category_fieldsets         = (((None, { 'fields': ('name', 'categories'),})), (log_fieldsets))
        category_list_display      = ('name',)
        category_readonly_fields   = ('update_by', 'date_create', 'date_update', 'error')
        category_filter_horizontal = ('categories',)
        articlecat_fieldsets       = (((None, { 'fields': ('category',),})), (log_fieldsets))
        articlecat_list_display    = ('list_html_br', 'category', 'author')
        articlecat_readonly_fields = ('update_by', 'date_create', 'date_update', 'error')
        articlecat_search_fields   = ('article__title', 'category__name')
        article_fieldsets          = (((None, { 'fields': ('language', 'title', 'content'),})), (log_fieldsets))
        article_readonly_fields    = ('update_by', 'date_create', 'date_update', 'error')
        language_fieldsets         = (((None, { 'fields': ('language','description'),})), (log_fieldsets))
        language_list_display      = ('language','description')
        language_readonly_fields   = ('update_by', 'date_create', 'date_update', 'error')

if hasattr(settings, Config.override):
    for config,configs in getattr(settings, Config.override).items():
        if hasattr(Config, config):
            for key,value in configs.items():
                if hasattr(getattr(Config, config), key):
                    setattr(getattr(Config, config), key, value)


class AuctorConfig(AppConfig, Config):
    name = 'auctor'
