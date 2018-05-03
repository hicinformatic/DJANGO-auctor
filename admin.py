from django.contrib import admin
from django.urls import re_path

from simplify.apps import SimplifyConfig as conf
from simplify.admin import OverAdmin

from .apps import AuctorConfig as aucconf
from .models import (Category, CategoryToArticle, Article, Language)
#from .forms import ProviderAdminForm
#from .views import (ProviderAdminCheck, GuestAdminCheck)

conf_path = {'ns': aucconf.namespace, 'ext': conf.extension.regex}

@admin.register(Language)
class CategoryAdmin(OverAdmin, admin.ModelAdmin):
    fieldsets       = aucconf.admin.language_fieldsets
    list_display    = aucconf.admin.language_list_display
    readonly_fields = aucconf.admin.language_readonly_fields

@admin.register(Category)
class CategoryAdmin(OverAdmin, admin.ModelAdmin):
    fieldsets       = aucconf.admin.category_fieldsets
    list_display    = aucconf.admin.category_list_display
    readonly_fields = aucconf.admin.category_readonly_fields
    filter_horizontal = aucconf.admin.category_filter_horizontal

class ArticleInline(admin.StackedInline):
    model = Article
    fieldsets = aucconf.admin.article_fieldsets
    readonly_fields = aucconf.admin.article_readonly_fields
@admin.register(CategoryToArticle)
class CategoryAdmin(OverAdmin, admin.ModelAdmin):
    fieldsets       = aucconf.admin.articlecat_fieldsets
    list_display    = aucconf.admin.articlecat_list_display
    readonly_fields = aucconf.admin.articlecat_readonly_fields
    inlines = [ArticleInline,]