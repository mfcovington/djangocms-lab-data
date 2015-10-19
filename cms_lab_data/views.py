from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .helpers import get_data_list_tags
from .menus import base_data_menu
from .models import DataFile, DataFileSet

def data_view(request):
    if request.toolbar:
        menu = base_data_menu(
            request.toolbar.get_or_create_menu('data-menu', 'Data')
        )

    context = {
        'data_file_count': DataFile.objects.filter(is_published=True).count(),
        'data_file_set_count': DataFileSet.objects.filter(
            is_published=True).count(),
    }
    return render(request, 'cms_lab_data/data.html', context)


class DataFileDetailView(DetailView):

    model = DataFile

    def get_context_data(self, **kwargs):
        if not self.object.is_published:
            raise Http404("Data file not published.")

        context = super().get_context_data(**kwargs)
        context['data_item'] = self.object
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar:
            menu = base_data_menu(
                self.request.toolbar.get_or_create_menu('data-menu', 'Data')
            )

            url_change = reverse('admin:cms_lab_data_datafile_change', args=[self.object.id])
            url_delete = reverse('admin:cms_lab_data_datafile_delete', args=[self.object.id])
            menu.add_modal_item('Edit %s' % self.object.name, url=url_change, position=0)
            menu.add_modal_item('Delete %s' % self.object.name, url=url_delete, position=1)
            menu.add_break(position=2)

        return super().render_to_response(context, **response_kwargs)


class DataFileListView(ListView):

    model = DataFile


    def get_context_data(self, **kwargs):
        data_list = self.object_list.filter(is_published=True)

        context = super().get_context_data(**kwargs)
        context.update({
            'data_list': data_list,
            'data_list_tags': get_data_list_tags(data_list),
            'label': 'Data Files',
            'pagination': 10,
            'searchable': True,
            'max_words': 40,
            'word_buffer': 10,
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar:
            menu = base_data_menu(
                self.request.toolbar.get_or_create_menu('data-menu', 'Data')
            )

        return super().render_to_response(context, **response_kwargs)


class DataFileSetDetailView(DetailView):

    model = DataFileSet

    def get_context_data(self, **kwargs):
        if not self.object.is_published:
            raise Http404("Data file set not published.")

        data_list = self.object.data_files.filter(is_published=True)

        context = super().get_context_data(**kwargs)
        context.update({
            'data_list': data_list,
            'data_list_tags': get_data_list_tags(data_list),
            'label': self.object.label,
            'pagination': 10,
            'searchable': True,
            'max_words': 40,
            'word_buffer': 10,
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar:
            menu = base_data_menu(
                self.request.toolbar.get_or_create_menu('data-menu', 'Data')
            )

            url_change = reverse('admin:cms_lab_data_datafileset_change', args=[self.object.id])
            url_delete = reverse('admin:cms_lab_data_datafileset_delete', args=[self.object.id])
            menu.add_modal_item('Edit %s' % self.object.name, url=url_change, position=0)
            menu.add_modal_item('Delete %s' % self.object.name, url=url_delete, position=1)
            menu.add_break(position=2)

        return super().render_to_response(context, **response_kwargs)


class DataFileSetListView(ListView):

    model = DataFileSet

    def get_context_data(self, **kwargs):
        data_list = self.object_list.filter(is_published=True)

        context = super().get_context_data(**kwargs)
        context.update({
            'is_data_file_set_list': True,
            'data_list': data_list,
            'data_list_tags': get_data_list_tags(data_list),
            'label': 'Data File Sets',
            'pagination': 10,
            'searchable': True,
            'max_words': 40,
            'word_buffer': 10,
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar:
            menu = base_data_menu(
                self.request.toolbar.get_or_create_menu('data-menu', 'Data')
            )

        return super().render_to_response(context, **response_kwargs)
