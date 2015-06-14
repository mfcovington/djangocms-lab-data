from django.contrib import admin
from django.db.models import Count

from .models import DataFile, DataFileSet
from taggit_helpers import (TaggitCounter, TaggitListFilter,
    TaggitTabularInline)


class DataFileSetInline(admin.TabularInline):
    model = DataFileSet.data_files.through
    extra = 3
    verbose_name = 'Associated Data File Set'
    verbose_name_plural = 'Associated Data File Sets'


@admin.register(DataFile)
class DataFileAdmin(TaggitCounter, admin.ModelAdmin):

    fieldset_data_file = ('Data File', {
        'fields': [
            'name',
            'file',
            'description',
        ],
    })

    fieldsets = [
        fieldset_data_file,
    ]

    inlines = [
        TaggitTabularInline,
        DataFileSetInline,
    ]

    list_display = (
        'name',
        'file',
        'description',
        'number_of_data_file_sets',
        'taggit_counter',
    )

    list_filter = (
        TaggitListFilter,
    )

    save_on_top = True

    search_fields = (
        'name',
        'file__name',
        'file__original_filename',
        'description',
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(data_file_set_count=Count('datafileset', distinct=True))
        return queryset

    def number_of_data_file_sets(self, obj):
        return obj.data_file_set_count
    number_of_data_file_sets.admin_order_field = 'data_file_set_count'
    number_of_data_file_sets.short_description = '# of Data File Sets'


@admin.register(DataFileSet)
class DataFileSetAdmin(TaggitCounter, admin.ModelAdmin):

    class Media:
        css = {
            'all': ('cms_lab_data/css/admin-publication-filter.css',)
        }

    fieldset_data_file_set = ('Data File Set', {
        'fields': [
            'name',
            'description',
            'image',
        ],
    })

    fieldset_data_files = ('Data Files', {
        'fields': [
            'data_files',
        ],
    })

    fieldsets = [
        fieldset_data_file_set,
        fieldset_data_files,
    ]

    filter_vertical = (
        'data_files',
    )

    inlines = [
        TaggitTabularInline,
    ]

    list_display = (
        'name',
        'description',
        'number_of_data_files',
        'taggit_counter',
    )

    list_filter = (
        TaggitListFilter,
    )

    save_on_top = True

    search_fields = (
        'name',
        'description',
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(data_file_count=Count('data_files', distinct=True))
        return queryset

    def number_of_data_files(self, obj):
        return obj.data_file_count
    number_of_data_files.admin_order_field = 'data_file_count'
    number_of_data_files.short_description = '# of Data Files'
