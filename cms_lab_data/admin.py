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


class ContentsPublishedFilter(admin.SimpleListFilter):
    """
    Filter Data File Set records by the presence of unpublished data files.
    """
    title = 'Contents Published'
    parameter_name = 'contents_published'

    def lookups(self, request, model_admin):
        return (
            ('all_published', 'Yes'),
            ('has_unpublished', 'Has Unpublished Content'),
        )

    def queryset(self, request, queryset):
        datasets_with_all_content_published = [
            ds.pk for ds in queryset
            if ds.data_files.count() == len(ds.published_data_files())
        ]

        if self.value() == 'all_published':
            return queryset.filter(pk__in=datasets_with_all_content_published)
        elif self.value() == 'has_unpublished':
            return queryset.exclude(pk__in=datasets_with_all_content_published)

@admin.register(DataFile)
class DataFileAdmin(TaggitCounter, admin.ModelAdmin):

    fieldset_data_file = ('Data File', {
        'fields': [
            'name',
            'slug',
            'file',
            'description',
            'is_published',
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
        'is_published',
    )

    list_filter = (
        'is_published',
        TaggitListFilter,
    )

    prepopulated_fields = {
        'slug': ('name',),
    }

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
            'slug',
            'label',
            'description',
            'image',
            'is_published',
        ],
    })

    fieldset_display_settings = ('Display Settings', {
        'fields': [
            'pagination',
            'max_words_file_description',
            'word_buffer_file_description',
            'searchable',
        ],
    })

    fieldset_data_files = ('Data Files', {
        'fields': [
            'data_files',
        ],
    })

    fieldsets = [
        fieldset_data_file_set,
        fieldset_display_settings,
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
        'label',
        'description',
        'number_of_data_files',
        'pagination',
        'max_words_file_description',
        'word_buffer_file_description',
        'taggit_counter',
        'searchable',
        'is_published',
        'contents_published',
    )

    list_filter = (
        'is_published',
        ContentsPublishedFilter,
        TaggitListFilter,
    )

    prepopulated_fields = {
        'slug': ('name',),
    }

    save_on_top = True

    search_fields = (
        'name',
        'label',
        'description',
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(data_file_count=Count('data_files', distinct=True))
        return queryset

    def contents_published(self, obj):
        if obj.data_file_count == len(obj.published_data_files()):
            return True
        else:
            return False
    contents_published.boolean = True
    contents_published.short_description = 'Contents published'

    def number_of_data_files(self, obj):
        return obj.data_file_count
    number_of_data_files.admin_order_field = 'data_file_count'
    number_of_data_files.short_description = '# of Data Files'
