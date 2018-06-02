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
class CategoryCreate(HybridCreateView):
    current_namespace = conf.namespace
    model = Category
    fields = ['name',]

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
class LanguageCreate(HybridCreateView):
    current_namespace = conf.namespace
    model = Language
    fields = ['language','description',]

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
class ArticleList(HybridListView):
    model = CategoryToArticle
    fields_detail = ['category', 'author', 'article']
    fields_relation = {'article': ['id','title', 'language'],}
    paginate_by = conf.paginate.article
    pk = 'list_html_br'

class ArticleDetail(HybridDetailView):
    model = CategoryToArticle
    fields_detail = ['id', 'list_html_pipe','category', 'author']

class ArticleThumbnail(HybridImageView):
    model = CategoryToArticle
    binary_field = 'thumbnail'
    title_field = 'id'
    prefix = 'auctor_thumbnail_'

class ArticleBanner(HybridImageView):
    model = CategoryToArticle
    binary_field = 'banner'
    title_field = 'id'
    prefix = 'auctor_banner_'

class Home(HybridListView):
    model = CategoryToArticle
    fields_detail = ['category', 'author', 'article',]
    fields_relation = {'article': ['id','title', 'language'],}
    paginate_by = conf.paginate.article
    pk = 'list_html_br'