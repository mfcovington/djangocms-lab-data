import collections
import operator

from django.core.urlresolvers import reverse

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import DataFileSetPlugin

class CMSDataFileSetPlugin(CMSPluginBase):
    model = DataFileSetPlugin
    module = 'Lab Plugins'
    name = 'Data File Set Plugin'
    render_template = 'cms_lab_data/plugin.html'

    def render(self, context, instance, placeholder):
        data_file_set_tags = {}
        data_file_set = instance.data_file_set.data_files.all()
        for data_file in data_file_set:
            for tag in data_file.tags.all():
                data_file_set_tags[tag.id] = tag.name
        data_file_set_tags = collections.OrderedDict(
            sorted(data_file_set_tags.items(), key=operator.itemgetter(1)))

        context.update({
            'instance': instance,
            'data_file_set_tags': data_file_set_tags,
        })

        menu = context['request'].toolbar.get_or_create_menu(
            'data-file-set-menu', 'Data File Set')

        url_change = reverse('admin:cms_lab_data_datafile_changelist')
        url_addnew = reverse('admin:cms_lab_data_datafile_add')
        menu.add_sideframe_item('Edit Data Files', url=url_change)
        menu.add_modal_item('Add New Data File', url=url_addnew)

        url_change = reverse('admin:cms_lab_data_datafileset_changelist')
        url_addnew = reverse('admin:cms_lab_data_datafileset_add')
        menu.add_sideframe_item('Edit Data File Sets', url=url_change)
        menu.add_modal_item('Add New Data File Set', url=url_addnew)

        return context

plugin_pool.register_plugin(CMSDataFileSetPlugin)
