from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import get_language, to_locale
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils import formats

from simplify.models import Update

from .apps import AuctorConfig as conf

# ██████╗ █████╗ ████████╗███████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗
#██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗██╔══██╗╚██╗ ██╔╝
#██║     ███████║   ██║   █████╗  ██║  ███╗██║   ██║██████╔╝ ╚████╔╝ 
#██║     ██╔══██║   ██║   ██╔══╝  ██║   ██║██║   ██║██╔══██╗  ╚██╔╝  
#╚██████╗██║  ██║   ██║   ███████╗╚██████╔╝╚██████╔╝██║  ██║   ██║   
# ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝
class Category(Update):
    name = models.CharField(conf.vn.name, help_text=conf.ht.name, max_length=254)
    categories = models.ManyToManyField('self', blank=True, help_text=conf.ht.categories)
    articles_nbr = models.PositiveIntegerField(conf.vn.articles_nbr, editable=False, default=0)
    enable = models.BooleanField(conf.vn.enable, default=True)
    delete = models.BooleanField(conf.vn.delete, default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = conf.vbn.category
        verbose_name_plural = conf.vpn.category

#██╗      █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗  ██████╗ ███████╗
#██║     ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██╔══██╗██╔════╝ ██╔════╝
#██║     ███████║██╔██╗ ██║██║  ███╗██║   ██║███████║██║  ███╗█████╗  
#██║     ██╔══██║██║╚██╗██║██║   ██║██║   ██║██╔══██║██║   ██║██╔══╝  
#███████╗██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝███████╗
#╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
class Language(Update):
    language = models.CharField(conf.vn.language, help_text=conf.ht.language, max_length=5, primary_key=True, default=conf.default.language)
    description = models.CharField(conf.vn.description, help_text=conf.ht.description, max_length=254, default=conf.default.language_desc)
    enable = models.BooleanField(conf.vn.enable, default=True)
    delete = models.BooleanField(conf.vn.delete, default=False)

    class Meta:
        verbose_name        = conf.vbn.language
        verbose_name_plural = conf.vpn.language

    def __str__(self):
        return '%s (%s)' % (self.description, self.language)

# █████╗ ██████╗ ████████╗██╗ ██████╗██╗     ███████╗
#██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝██║     ██╔════╝
#███████║██████╔╝   ██║   ██║██║     ██║     █████╗  
#██╔══██║██╔══██╗   ██║   ██║██║     ██║     ██╔══╝  
#██║  ██║██║  ██║   ██║   ██║╚██████╗███████╗███████╗
#╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝╚══════╝╚══════╝
class CategoryToArticle(Update):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(conf.vn.author, blank=True, editable=False, help_text=conf.ht.author, max_length=254, null=True)
    comments_nbr = models.PositiveIntegerField(conf.vn.comments_nbr, editable=False, default=0)
    thumbnail = models.BinaryField(null=True)
    thumbnail_mimetype = models.CharField(max_length=20, null=True, blank=True)
    banner = models.BinaryField(null=True)
    banner_mimetype = models.CharField(max_length=20, null=True, blank=True)
    keywords = models.TextField(conf.vn.keywords, blank=True, editable=False, help_text=conf.ht.keywords, max_length=254, null=True)
    locale = to_locale(get_language())[:2]

    class Meta:
        verbose_name        = conf.vbn.article
        verbose_name_plural = conf.vpn.article
        permissions  = (
            ('can_get_banner', conf.ht.can_get_banner),
            ('can_get_thumbnail', conf.ht.can_get_thumbnail),
        )

    def list_html_br(self):
        articles = self.article_set.all()
        if articles.count() > 0: 
            return format_html('<br>'.join(str(i) for i in articles.values_list('title', flat=True)))
        return conf.message.norelatedarticles
    list_html_br.short_description = conf.ht.list_html_br

    def list_html_pipe(self):
        articles = self.article_set.all()
        if articles.count() > 0: 
            return ' | '.join(str(i) for i in articles.values_list('title', flat=True))
        return conf.message.norelatedarticles
    list_html_pipe.short_description = conf.ht.list_html_pipe

    def first_article(self):
        try:
            return self.article_set.first()
        except AttributeError:
            return conf.message.norelatedarticles
    first_article.short_description = conf.ht.first_article

    def article_language(self):
        articles = self.article_set.filter(language=self.locale)
        if articles.count() > 0:
            return articles[0]
        return conf.message.norelatedarticles_languages
    article_language.short_description = conf.ht.article_language

    def get_thumbnail(self):
        if self.thumbnail is not None:
            url = reverse('auctor:article-thumbnail',  args=[self.id, conf.default.thumbnail[self.thumbnail_mimetype]])
            return format_html('<a class="button" href="{url}">{vn}</a>'.format(url=url, vn=conf.vn.get_thumbnail))
        return format_html('<a class="button" style="background: gray" href="">{vn}</a>'.format(vn=conf.vn.get_thumbnail))
    get_thumbnail.short_description = conf.vn.get_thumbnail

    def get_banner(self):
        if self.banner is not None:
            url = reverse('auctor:article-banner',  args=[self.id, conf.default.banner[self.banner_mimetype]])
            return format_html('<a class="button" href="{url}">{vn}</a>'.format(url=url, vn=conf.vn.get_banner))
        return format_html('<a class="button" style="background: gray" href="">{vn}</a>'.format(vn=conf.vn.get_banner))
    get_banner.short_description = conf.vn.get_banner

    def static_thumbnail(self):
        if self.thumbnail_mimetype is not None and self.thumbnail is not None:
            formatted_datetime = formats.date_format(self.date_create, 'Ymd')
            extend = conf.default.banner[self.thumbnail_mimetype]
            return static('auctor/{date}/thumbnail_{pk}.{ext}'.format(date=formatted_datetime, pk=self.pk, ext=extend))
        return None
    static_thumbnail.short_description = conf.vn.static_thumbnail

    def static_banner(self):
        if self.banner_mimetype is not None and self.banner is not None:
            formatted_datetime = formats.date_format(self.date_create, 'Ymd')
            extend = conf.default.banner[self.banner_mimetype]
            return static('auctor/{date}/banner_{pk}.{ext}'.format(date=formatted_datetime, pk=self.pk, ext=extend))
        return None
    static_banner.short_description = conf.vn.static_banner

class Article(Update):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=conf.default.language)
    category = models.ForeignKey(CategoryToArticle, on_delete=models.CASCADE)
    title = models.CharField(conf.vn.title, help_text=conf.ht.title, max_length=254)
    keywords = models.CharField(conf.vn.keywords, blank=True, help_text=conf.ht.keywords, max_length=254, null=True)
    content = models.TextField(conf.vn.content, help_text=conf.ht.content, blank=True, null=True)
    comments_nbr = models.PositiveIntegerField(conf.vn.comments_nbr, editable=False, default=0)
    enable = models.BooleanField(conf.vn.enable, default=True)
    delete = models.BooleanField(conf.vn.delete, default=False)

    class Meta:
        verbose_name        = conf.vbn.article
        verbose_name_plural = conf.vpn.article
        ordering = ['-date_create']

    def __str__(self):
        return self.title

    def content_cut(self):
        return '%s...' % self.content[:150] if len(self.content) > 150 else self.content

# ██████╗ ██████╗ ███╗   ███╗███╗   ███╗███████╗███╗   ██╗████████╗
#██╔════╝██╔═══██╗████╗ ████║████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
#██║     ██║   ██║██╔████╔██║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
#██║     ██║   ██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
#╚██████╗╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
# ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝
class Comment(Update):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, editable=False)
    content = models.TextField(conf.vn.content, help_text=conf.ht.content, blank=True, null=True)
    author = models.CharField(conf.vn.author, blank=True, editable=False, help_text=conf.ht.author, max_length=254, null=True)
    censor = models.BooleanField(conf.vn.censor, default=False)
    delete = models.BooleanField(conf.vn.delete, default=False)

    class Meta:
        verbose_name        = conf.vbn.comment
        verbose_name_plural = conf.vpn.comment

    def __str__(self):
        return self.content
