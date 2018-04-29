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

class Article(Update):
    article = models.ForeignKey(CategoryToArticle, on_delete=models.CASCADE)
    title = models.CharField(conf.vn.title, help_text=conf.ht.title, max_length=254)

    def __str__(self):
        return self.title