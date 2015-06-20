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


class DataFileSetDetailView(DetailView):

    model = DataFileSet


class DataFileSetListView(ListView):

    model = DataFileSet
