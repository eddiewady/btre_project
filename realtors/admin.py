from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone', 'email', 'hire_date', 'is_mvp')
  list_display_links = ('name', 'phone', 'email', 'hire_date')
  list_filter = ('name',)
  list_editable = ('is_mvp',)
  search_fields = ('name', 'phone', 'email', 'hire_date')
  list_per_page = 25
admin.site.register(Realtor,RealtorAdmin)
