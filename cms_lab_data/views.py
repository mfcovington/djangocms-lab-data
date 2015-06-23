from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .helpers import get_data_file_list_tags
from .menus import base_data_menu
from .models import DataFile, DataFileSet

def data_view(request):
    if request.toolbar:
        menu = base_data_menu(request, 'data-menu', 'Data')

    context = {
        'data_file_count': DataFile.objects.count(),
        'data_file_set_count': DataFileSet.objects.count(),
    }
    return render(request, 'cms_lab_data/data.html', context)


class DataFileDetailView(DetailView):

    model = DataFile

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar:
            menu = base_data_menu(self.request, 'data-menu', 'Data')

            url_change = reverse('admin:cms_lab_data_datafile_change', args=[self.object.id])
            url_delete = reverse('admin:cms_lab_data_datafile_delete', args=[self.object.id])
            menu.add_modal_item('Edit %s' % self.object.name, url=url_change, position=0)
            menu.add_modal_item('Delete %s' % self.object.name, url=url_delete, position=1)
            menu.add_break(position=2)

        return super().render_to_response(context, **response_kwargs)


class DataFileListView(ListView):

    model = DataFile


    def get_context_data(self, **kwargs):
        data_file_list = self.object_list

        context = super(DataFileListView, self).get_context_data(**kwargs)
        context.update({
            'data_file_set': data_file_list,
            'data_file_set_tags': get_data_file_list_tags(data_file_list),
            'label': 'Data Files',
            'pagination': 10,
            'searchable': True,
            'max_words': 40,
            'word_buffer': 10,
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar:
            menu = base_data_menu(self.request, 'data-menu', 'Data')

        return super().render_to_response(context, **response_kwargs)


class DataFileSetDetailView(DetailView):

    model = DataFileSet

    def get_context_data(self, **kwargs):
        data_file_list = self.object.data_files.all()

        context = super(DataFileSetDetailView, self).get_context_data(**kwargs)
        context.update({
            'data_file_set': data_file_list,
            'data_file_set_tags': get_data_file_list_tags(data_file_list),
            'label': self.object.label,
            'pagination': 10,
            'searchable': True,
            'max_words': 40,
            'word_buffer': 10,
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar:
            menu = base_data_menu(self.request, 'data-menu', 'Data')

            url_change = reverse('admin:cms_lab_data_datafileset_change', args=[self.object.id])
            url_delete = reverse('admin:cms_lab_data_datafileset_delete', args=[self.object.id])
            menu.add_modal_item('Edit %s' % self.object.name, url=url_change, position=0)
            menu.add_modal_item('Delete %s' % self.object.name, url=url_delete, position=1)
            menu.add_break(position=2)

        return super().render_to_response(context, **response_kwargs)


class DataFileSetListView(ListView):

    model = DataFileSet

    def get_context_data(self, **kwargs):
        data_file_list = self.object_list

        context = super(DataFileSetListView, self).get_context_data(**kwargs)
        context.update({
            'is_data_file_set_list': True,
            'data_file_set': data_file_list,
            'data_file_set_tags': get_data_file_list_tags(data_file_list),
            'label': 'Data File Sets',
            'pagination': 10,
            'searchable': True,
            'max_words': 40,
            'word_buffer': 10,
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar:
            menu = base_data_menu(self.request, 'data-menu', 'Data')

        return super().render_to_response(context, **response_kwargs)
