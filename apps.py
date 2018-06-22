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
        static_root  = settings.STATIC_ROOT
        images = 'auctor'

    class message(object):
        norelatedarticles = _('No related articles')
        norelatedarticles_languages = _('No related article in your favorite languages')

    class error(object):
        mimetype_thumbnail = _('Mimetype not allowed: %s')
        mimetype_banner = _('Mimetype not allowed: %s')
        size_thumbnail = _('The file size exceeds the size allowed: %s > %s')
        size_banner = _('The file size exceeds the size allowed: %s > %s')

    class vn(object):
        name = _('Category name')
        categories = _('Sub categories')
        articles_nbr = _('Number of articles')
        title = _('Title')
        content_ac = _('Content Auctor-Code')
        content = _('Content')
        author = _('Author')
        keywords = _('Keywords')
        language = _('Language')
        description = _('Description')
        comments_nbr = _('Number of comments')
        state = _('Status')
        get_thumbnail = _('Thumbnail')
        static_thumbnail = _('URL static thumbnail')
        root_thumbnail = _('Path root thumbnail')
        get_banner = _('Banner')
        static_banner = _('URL static banner')
        root_banner = _('Path root banner')

    class ht(object):
        name = _('Name of the category')
        categories = _('Sub categories')
        title = _('Article title')
        content_ac = _('Article Content Auctor-Code')
        content = _('Article content')
        author = _('Article author')
        keywords = _('keywords separated by a space')
        language = _('Language')
        description = _('Description')
        list_html_br = _('Articles')
        list_html_pipe = _('Articles')
        first_article = _('First article')
        article_language = _('Article in your favorite language')
        can_get_banner = _('Can get banner')
        can_get_thumbnail = _('Can get thumbnail')
        can_get_full = _('Can get full')
        browser_language = _('Browser')

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

    class choices(object):
        state_preview = 'PREVIEW'
        state_enable = 'ENABLE'
        state_censor = 'CENSOR'
        state_delete = 'DELETE'
        state_approbate = 'APPROBATE'
        state_validate = 'VALIDATE'
        state = (
            (state_preview,  _('Preview')),
            (state_enable,  _('Enable')),
            (state_censor,  _('Censored')),
            (state_delete,  _('Deleted')),
            (state_approbate, _('In approbation')),
            (state_validate, _('Validated')),
        )

    class default(object):
        language = 'fr'
        language_desc = 'Français'
        thumbnail = {'image/jpeg': 'jpg', 'image/pjpeg': 'jpg', 'image/png': 'png', 'image/x-png': 'png', 'image/svg+xml': 'svg'}
        thumbnail_size = 400000
        banner = {'image/jpeg': 'jpg', 'image/pjpeg': 'jpg', 'image/png': 'png', 'image/x-png': 'png', 'image/svg+xml': 'svg'}
        banner_size = 1000000
        library_pil = False
        thumbnail_img = 'img/commons/thumbnail.svg'
        banner_img = 'img/commons/default.svg'

    class admin(object):
        log_fieldsets              = (_('Log informations'), {'fields': ('update_by', 'date_create', 'date_update', 'error', 'message')})
        category_fieldsets         = (((None, { 'fields': ('name', 'state', 'categories'),})), (log_fieldsets))
        category_list_display      = ('name', 'articles_nbr', 'state')
        category_readonly_fields   = ('articles_nbr', 'update_by', 'date_create', 'date_update', 'error')
        category_filter_horizontal = ('categories',)
        category_list_filter       = ('state',)
        articlecat_fieldsets       = (((None, { 'fields': ('category', 'comments_nbr', 'thumbnail_img', 'thumbnail_mimetype', 'banner_img', 'banner_mimetype', 'keywords'),})), (log_fieldsets))
        articlecat_list_display    = ('list_html_br', 'category', 'author', 'comments_nbr', 'first_article', 'article_language', 'button_get_thumbnail', 'button_get_banner')
        articlecat_readonly_fields = ('comments_nbr', 'update_by', 'date_create', 'date_update', 'error', 'keywords')
        articlecat_search_fields   = ('article__title', 'category__name', 'keywords')
        article_fieldsets          = (((None, { 'fields': ('language', 'title', 'keywords', 'state', 'content_ac', 'content', 'comments_nbr'),})), (log_fieldsets))
        article_readonly_fields    = ('comments_nbr', 'update_by', 'date_create', 'date_update', 'error')
        language_fieldsets         = (((None, { 'fields': ('language', 'description', 'state'),})), (log_fieldsets))
        language_list_display      = ('language', 'browser_language','description', 'state')
        language_readonly_fields   = ('update_by', 'date_create', 'date_update', 'error')
        language_list_filter       = ('state',)
        language_search_fields     = ('language', 'description')
        comment_fieldsets         = (((None, { 'fields': ('article','state', 'content', 'author'),})), (log_fieldsets))
        comment_list_display      = ('content', 'author', 'article', 'state')
        comment_readonly_fields   = ('article', 'author', 'update_by', 'date_create', 'date_update', 'error')
        comment_list_filter       = ('state',)

    class paginate(object):
        category = 25
        article = 2
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

    def ready(self):
        from . import signals