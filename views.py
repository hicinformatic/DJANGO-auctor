from django.contrib import messages
from django.contrib.auth.decorators import (permission_required , login_required)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from simplify.hybrids import (FakeModel, HybridAdminView, HybridCreateView, HybridUpdateView, HybridDetailView, HybridListView, HybridTemplateView)
from simplify.decorators import is_superuser_required

from .apps import AuctorConfig as conf
from .models import (Category, CategoryToArticle, Article, Language)

class CategoryCreate(HybridCreateView):
    model = Category
    fields = ['name',]

class CategoryUpdate(HybridUpdateView):
    model = Category
    fields = ['name',]

class CategoryList(HybridListView):
    model = Category
    fields_detail = ['id', 'name',]
    paginate_by = conf.paginate.category

class CategoryDetail(HybridDetailView):
    model = Category
    fields_detail = ['id', 'name',]

class LanguageCreate(HybridCreateView):
    model = Language
    fields = ['language','description',]

class LanguageUpdate(HybridUpdateView):
    model = Language
    fields = ['language','description',]

class LanguageList(HybridListView):
    model = Language
    fields_detail = ['language','description',]

class LanguageDetail(HybridDetailView):
    model = Language
    fields_detail = ['language','description',]

class ArticleList(HybridListView):
    model = CategoryToArticle
    fields_detail = ['id', 'list_html_pipe','category', 'author', 'article']
    fields_relation = {'article': ['id','title', 'langue'],}
    paginate_by = conf.paginate.article

class ArticleDetail(HybridDetailView):
    model = CategoryToArticle
    fields_detail = ['id', 'list_html_pipe','category', 'author']

