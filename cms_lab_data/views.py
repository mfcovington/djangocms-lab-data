from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .helpers import get_data_file_list_tags
from .models import DataFile, DataFileSet

def data_view(request):
    context = {
        'data_file_count': DataFile.objects.count(),
        'data_file_set_count': DataFileSet.objects.count(),
    }
    return render(request, 'cms_lab_data/data.html', context)


class DataFileDetailView(DetailView):

    model = DataFile


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
