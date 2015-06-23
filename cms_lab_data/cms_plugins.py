import collections
import operator

from django.core.urlresolvers import reverse

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .helpers import get_data_file_list_tags
from .menus import base_data_menu
from .models import DataFileSetPlugin


class CMSDataFileSetPlugin(CMSPluginBase):
    model = DataFileSetPlugin
    module = 'Lab Plugins'
    name = 'Data File Set Plugin'
    render_template = 'cms_lab_data/plugin.html'

    def render(self, context, instance, placeholder):
        data_file_set = instance.data_file_set
        data_file_list = data_file_set.data_files.all()

        menu = base_data_menu(context['request'].toolbar.get_or_create_menu(
            'data-menu', 'Data'))

        context.update({
            'data_file_set': data_file_list,
            'data_file_set_tags': get_data_file_list_tags(data_file_list),
            'unique_id': 's{}i{}'.format(data_file_set.id, instance.id),
            'label': data_file_set.label,
            'pagination': data_file_set.pagination,
            'searchable': data_file_set.searchable,
            'max_words': data_file_set.max_words_file_description,
            'word_buffer': data_file_set.word_buffer_file_description,
        })

        return context

plugin_pool.register_plugin(CMSDataFileSetPlugin)
