from django.contrib import admin
from django.urls import re_path

from simplify.apps import SimplifyConfig as conf
from simplify.admin import OverAdmin

from .apps import AuctorConfig as aucconf
from .models import (Category)
#from .forms import ProviderAdminForm
#from .views import (ProviderAdminCheck, GuestAdminCheck)

conf_path = {'ns': aucconf.namespace, 'ext': conf.extension.regex}

@admin.register(Category)
class CategoryAdmin(OverAdmin, admin.ModelAdmin):
    fieldsets       = aucconf.admin.category_fieldsets
    list_display    = aucconf.admin.category_list_display
    readonly_fields = aucconf.admin.category_readonly_fields
    filter_horizontal = aucconf.admin.category_filter_horizontal
