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

    class message(object):
        norelatedarticles = _('No related articles')
        norelatedarticles_languages = _('No related articles in your favorite languages')

    class vn(object):
        name = _('Category name')
        categories = _('Sub categories')
        articles_nbr = _('Number of articles')
        title = _('Title')
        content = _('Content')
        author = _('Author')
        keywords = _('Keywords')
        language = _('Language')
        description = _('Description')
        comments_nbr = _('Number of comments')
        enable = _('Enabled')
        censor = _('Censored')
        delete = _('Deleted')

    class ht(object):
        name = _('Name of the category')
        categories = _('Sub categories')
        title = _('Article title')
        content = _('Article content')
        author = _('Article author')
        keywords = _('keywords separated by a space')
        language = _('Language')
        description = _('Description')
        list_html_br = _('Articles')
        list_html_pipe = _('Articles')
        first_article = _('First article')
        article_language = _('Article in your favorite language')

    class vbn(object):
        category = _('Category')
        article = _('Article')
        language = _('Language')
        comment = _('Comment')

    class vpn(object):
        category = _('Categories')
        article = _('Articles')
        language = _('Languages')
        comment = _('Comments')

    class default(object):
        language = 'fr'
        language_desc = 'Français'

    class admin(object):
        log_fieldsets              = (_('Log informations'), {'fields': ('update_by', 'date_create', 'date_update', 'error', 'message')})
        category_fieldsets         = (((None, { 'fields': ('name', 'enable', 'delete', 'categories'),})), (log_fieldsets))
        category_list_display      = ('name', 'articles_nbr', 'enable', 'delete')
        category_readonly_fields   = ('articles_nbr', 'update_by', 'date_create', 'date_update', 'error')
        category_filter_horizontal = ('categories',)
        category_list_filter       = ('enable', 'delete')
        articlecat_fieldsets       = (((None, { 'fields': ('category', 'comments_nbr','thumbnail_img', 'banner_img',),})), (log_fieldsets))
        articlecat_list_display    = ('list_html_br', 'category', 'author', 'comments_nbr', 'first_article', 'article_language')
        articlecat_readonly_fields = ('comments_nbr', 'update_by', 'date_create', 'date_update', 'error')
        articlecat_search_fields   = ('article__title', 'category__name')
        article_fieldsets          = (((None, { 'fields': ('language', 'title', 'keywords', 'enable', 'delete', 'content', 'comments_nbr'),})), (log_fieldsets))
        article_readonly_fields    = ('comments_nbr', 'update_by', 'date_create', 'date_update', 'error')
        article_list_filter        = ('enable', 'delete')
        language_fieldsets         = (((None, { 'fields': ('language', 'description', 'enable', 'delete'),})), (log_fieldsets))
        language_list_display      = ('language','description', 'enable', 'delete')
        language_readonly_fields   = ('update_by', 'date_create', 'date_update', 'error')
        language_list_filter       = ('enable', 'delete')
        comment_fieldsets         = (((None, { 'fields': ('article','censor', 'delete', 'content', 'author'),})), (log_fieldsets))
        comment_list_display      = ('content', 'author', 'article', 'censor', 'delete')
        comment_readonly_fields   = ('article', 'author', 'update_by', 'date_create', 'date_update', 'error')
        comment_list_filter       = ('censor', 'delete')

    class paginate(object):
        category = 25
        article = 25
        comment = 25

    class template(object):
        home  = 'auctor/{ext}/home.{ext}'

if hasattr(settings, Config.override):
    for config,configs in getattr(settings, Config.override).items():
        if hasattr(Config, config):
            for key,value in configs.items():
                if hasattr(getattr(Config, config), key):
                    setattr(getattr(Config, config), key, value)


class AuctorConfig(AppConfig, Config):
    name = 'auctor'
