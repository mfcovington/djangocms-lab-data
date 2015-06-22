import collections
import operator

from django.shortcuts import render
from django.views.generic import DetailView, ListView

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
        context = super(DataFileListView, self).get_context_data(**kwargs)

        data_file_set_tags = {}
        for tag in DataFile.tags.all():
            data_file_set_tags[tag.id] = tag.name

        data_file_set_tags = collections.OrderedDict(
            sorted(data_file_set_tags.items(), key=operator.itemgetter(1)))

        context['data_file_set'] = DataFile.objects.all()
        context['data_file_set_tags'] = data_file_set_tags
        context['label'] = 'Data Files'
        context['pagination'] = 10
        context['searchable'] = True
        context['max_words'] = 40
        context['word_buffer'] = 10
        return context


class DataFileSetDetailView(DetailView):

    model = DataFileSet

    def get_context_data(self, **kwargs):
        context = super(DataFileSetDetailView, self).get_context_data(**kwargs)

        data_file_set_tags = {}
        data_file_set = self.object.data_files.all()
        for data_file in data_file_set:
            for tag in data_file.tags.all():
                data_file_set_tags[tag.id] = tag.name

        data_file_set_tags = collections.OrderedDict(
            sorted(data_file_set_tags.items(), key=operator.itemgetter(1)))


        context['data_file_set'] = data_file_set
        context['data_file_set_tags'] = data_file_set_tags
        context['label'] = self.object.label
        context['pagination'] = 10
        context['searchable'] = True
        context['max_words'] = 40
        context['word_buffer'] = 10
        return context


class DataFileSetListView(ListView):

    model = DataFileSet
