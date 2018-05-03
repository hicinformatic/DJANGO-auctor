from django.db import models
from django.urls import reverse
from django.utils.html import format_html

from simplify.models import Update

from .apps import AuctorConfig as conf

class Category(Update):
    name = models.CharField(conf.vn.name, help_text=conf.ht.name, max_length=254)
    categories = models.ManyToManyField('self', blank=True, help_text=conf.ht.categories)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = conf.vbn.category
        verbose_name_plural = conf.vpn.category

class CategoryToArticle(Update):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name        = conf.vbn.article
        verbose_name_plural = conf.vpn.article

class Language(Update):
    language = models.CharField(conf.vn.language, help_text=conf.ht.language, max_length=5, primary_key=True, default=conf.default.language)
    description = models.CharField(conf.vn.description, help_text=conf.ht.description, max_length=254)

    class Meta:
        verbose_name        = conf.vbn.language
        verbose_name_plural = conf.vpn.language

    def __str__(self):
        return '%s (%s)' % (self.description, self.language)

class Article(Update):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=conf.default.language)
    category = models.ForeignKey(CategoryToArticle, on_delete=models.CASCADE)
    title = models.CharField(conf.vn.title, help_text=conf.ht.title, max_length=254)
    content = models.TextField(conf.vn.content, help_text=conf.ht.content, blank=True, null=True)

    def __str__(self):
        return self.title