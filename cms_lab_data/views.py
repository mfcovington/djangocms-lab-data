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

        context['data_file_set_tags'] = data_file_set_tags
        context['pagination'] = 10
        context['searchable'] = True
        context['max_words'] = 40
        context['word_buffer'] = 10
        return context


class DataFileSetDetailView(DetailView):

    model = DataFileSet


class DataFileSetListView(ListView):

    model = DataFileSet
