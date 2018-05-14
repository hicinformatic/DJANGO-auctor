from django.urls import path, re_path

from simplify.apps import SimplifyConfig as conf
from .apps import AuctorConfig as aucconf
from . import views

conf_path = {'ns': aucconf.namespace, 'ext': conf.extension.regex}
urlpatterns = []

urlpatterns.append(re_path(r'{ns}/category/create(\.|/)?(?P<extension>({ext}))?/?'.format(**conf_path), views.CategoryCreate.as_view(), name='category-create'))
urlpatterns.append(re_path(r'{ns}/category/(?P<pk>\d+)/update(\.|/)?(?P<extension>({ext}))?/?'.format(**conf_path), views.CategoryUpdate.as_view(), name='category-update'))
urlpatterns.append(re_path(r'{ns}/category/(?P<pk>\d+)/detail(\.|/)?(?P<extension>({ext}))?/?'.format(**conf_path), views.CategoryDetail.as_view(), name='category-detail'))
urlpatterns.append(re_path(r'{ns}/category/list(\.|/)?(?P<extension>({ext}))?/?'.format(**conf_path), views.CategoryList.as_view(), name='category-list'))

urlpatterns.append(re_path(r'{ns}/language/create(\.|/)?(?P<extension>({ext}))?/?'.format(**conf_path), views.LanguageCreate.as_view(), name='language-create'))
urlpatterns.append(re_path(r'{ns}/language/(?P<pk>\w+)/update(\.|/)?(?P<extension>({ext}))?/?'.format(**conf_path), views.LanguageUpdate.as_view(), name='language-update'))
urlpatterns.append(re_path(r'{ns}/language/(?P<pk>\w+)/detail(\.|/)?(?P<extension>({ext}))?/?'.format(**conf_path), views.LanguageDetail.as_view(), name='language-detail'))
urlpatterns.append(re_path(r'{ns}/language/list(\.|/)?(?P<extension>({ext}))?/?'.format(**conf_path), views.LanguageList.as_view(), name='language-list'))

urlpatterns.append(re_path(r'{ns}/article/(?P<pk>\w+)/detail(\.|/)?(?P<extension>({ext}))?/?'.format(**conf_path), views.ArticleDetail.as_view(), name='article-detail'))
urlpatterns.append(re_path(r'{ns}/article/list(\.|/)?(?P<extension>({ext}))?/?'.format(**conf_path), views.ArticleList.as_view(), name='article-list'))