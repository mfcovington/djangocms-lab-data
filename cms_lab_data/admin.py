from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models import Count

from .models import DataFile, DataFileSet
from taggit.models import TaggedItem


class DataFileSetInline(admin.TabularInline):
    model = DataFileSet.data_files.through
    extra = 3
    verbose_name = 'Associated Data File Set'
    verbose_name_plural = 'Associated Data File Sets'


class TaggedItemInline(GenericTabularInline):
    model = TaggedItem
    verbose_name = 'Tag'
    verbose_name_plural = 'Tags'
    ordering = ('tag__name',)


@admin.register(DataFile)
class DataFileAdmin(admin.ModelAdmin):

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
        TaggedItemInline,
        DataFileSetInline,
    ]

    list_display = (
        'name',
        'file',
        'description',
        'number_of_data_file_sets',
        'number_of_tags',
    )

    save_on_top = True

    search_fields = (
        'name',
        'file__name',
        'file__original_filename',
        'description',
    )

    def queryset(self, request):
        queryset = super().queryset(request)
        queryset = queryset.annotate(data_file_set_count=Count('datafileset', distinct=True))
        queryset = queryset.annotate(tag_count=Count('tags', distinct=True))
        return queryset

    def number_of_data_file_sets(self, obj):
        return obj.data_file_set_count
    number_of_data_file_sets.admin_order_field = 'data_file_set_count'
    number_of_data_file_sets.short_description = '# of Data File Sets'

    def number_of_tags(self, obj):
        return obj.tag_count
    number_of_tags.admin_order_field = 'tag_count'
    number_of_tags.short_description = '# of Tags'


@admin.register(DataFileSet)
class DataFileSetAdmin(admin.ModelAdmin):

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
        TaggedItemInline,
    ]

    list_display = (
        'name',
        'description',
        'number_of_data_files',
        'number_of_tags',
    )

    save_on_top = True

    search_fields = (
        'name',
        'description',
    )

    def queryset(self, request):
        queryset = super().queryset(request)
        queryset = queryset.annotate(data_file_count=Count('data_files', distinct=True))
        queryset = queryset.annotate(tag_count=Count('tags', distinct=True))
        return queryset

    def number_of_data_files(self, obj):
        return obj.data_file_count
    number_of_data_files.admin_order_field = 'data_file_count'
    number_of_data_files.short_description = '# of Data Files'

    def number_of_tags(self, obj):
        return obj.tag_count
    number_of_tags.admin_order_field = 'tag_count'
    number_of_tags.short_description = '# of Tags'
