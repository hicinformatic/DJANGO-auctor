from django.contrib import messages
from django.contrib.auth.decorators import (permission_required , login_required)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from simplify.hybrids import (FakeModel, HybridAdminView, HybridCreateView, HybridUpdateView, HybridDetailView, HybridListView, HybridTemplateView, HybridImageView)
from simplify.decorators import is_superuser_required

from .apps import AuctorConfig as conf
from .models import (Category, CategoryToArticle, Article, Language)

# ██████╗ █████╗ ████████╗███████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗
#██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗██╔══██╗╚██╗ ██╔╝
#██║     ███████║   ██║   █████╗  ██║  ███╗██║   ██║██████╔╝ ╚████╔╝ 
#██║     ██╔══██║   ██║   ██╔══╝  ██║   ██║██║   ██║██╔══██╗  ╚██╔╝  
#╚██████╗██║  ██║   ██║   ███████╗╚██████╔╝╚██████╔╝██║  ██║   ██║   
# ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝
@method_decorator(permission_required('auctor.add_category'), name='dispatch')
class CategoryCreate(HybridCreateView):
    current_namespace = conf.namespace
    model = Category
    fields = ['name',]

@method_decorator(permission_required('auctor.change_category'), name='dispatch')
class CategoryUpdate(HybridUpdateView):
    current_namespace = conf.namespace
    model = Category
    fields = ['name',]

class CategoryList(HybridListView):
    model = Category
    fields_detail = ['id', 'name',]
    paginate_by = conf.paginate.category

class CategoryDetail(HybridDetailView):
    model = Category
    fields_detail = ['id', 'name',]

#██╗      █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗  ██████╗ ███████╗
#██║     ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██╔══██╗██╔════╝ ██╔════╝
#██║     ███████║██╔██╗ ██║██║  ███╗██║   ██║███████║██║  ███╗█████╗  
#██║     ██╔══██║██║╚██╗██║██║   ██║██║   ██║██╔══██║██║   ██║██╔══╝  
#███████╗██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝███████╗
#╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
@method_decorator(permission_required('auctor.add_language'), name='dispatch')
class LanguageCreate(HybridCreateView):
    current_namespace = conf.namespace
    model = Language
    fields = ['language','description',]

@method_decorator(permission_required('auctor.change_language'), name='dispatch')
class LanguageUpdate(HybridUpdateView):
    current_namespace = conf.namespace
    model = Language
    fields = ['language','description',]

class LanguageList(HybridListView):
    model = Language
    fields_detail = ['language','description',]

class LanguageDetail(HybridDetailView):
    model = Language
    fields_detail = ['language','description',]

# █████╗ ██████╗ ████████╗██╗ ██████╗██╗     ███████╗
#██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝██║     ██╔════╝
#███████║██████╔╝   ██║   ██║██║     ██║     █████╗  
#██╔══██║██╔══██╗   ██║   ██║██║     ██║     ██╔══╝  
#██║  ██║██║  ██║   ██║   ██║╚██████╗███████╗███████╗
#╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝╚══════╝╚══════╝
@method_decorator(permission_required('auctor.can_get_full'), name='dispatch')
class ArticleListFull(HybridListView):
    model = CategoryToArticle
    fields_detail = ['id', 'category', 'author', 'article', 'first_article', 'article_language', 'get_thumbnail', 'root_thumbnail', 'get_banner', 'root_banner']
    fields_relation = {'article': ['id','title', 'language', 'content_cut'], }
    paginate_by = conf.paginate.article
    pk = 'list_html_br'

class ArticleList(HybridListView):
    model = CategoryToArticle
    fields_detail = ['category', 'author', 'article', 'first_article', 'article_language']
    fields_relation = {'article': ['id','title', 'language', 'content_cut'], }
    paginate_by = conf.paginate.article
    pk = 'list_html_br'

class ArticleDetail(HybridDetailView):
    model = CategoryToArticle
    fields_detail = ['id', 'list_html_pipe','category', 'author']

@method_decorator(permission_required('auctor.can_get_thumbnail'), name='dispatch')
class ArticleThumbnail(HybridImageView):
    model = CategoryToArticle
    binary_field = 'thumbnail'
    title_field = 'id'
    prefix = 'auctor_thumbnail_'

@method_decorator(permission_required('auctor.can_get_banner'), name='dispatch')
class ArticleBanner(HybridImageView):
    model = CategoryToArticle
    binary_field = 'banner'
    title_field = 'id'
    prefix = 'auctor_banner_'

class Home(HybridListView):
    model = CategoryToArticle
    fields_detail = ['category', 'author', 'article', 'first_article',]
    fields_relation = {'article': ['id','title', 'language'], 'first_article': ['id','title', 'language']}
    paginate_by = conf.paginate.article
    pk = 'list_html_br'
    template_name = conf.template.home