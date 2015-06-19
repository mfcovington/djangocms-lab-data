from django.views.generic import DetailView, ListView

from .models import DataFile, DataFileSet

class DataFileDetailView(DetailView):

    model = DataFile


class DataFileListView(ListView):

    model = DataFile


class DataFileSetDetailView(DetailView):

    model = DataFileSet


class DataFileSetListView(ListView):

    model = DataFileSet
