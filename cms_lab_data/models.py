from django.db import models

from cms.models import CMSPlugin
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from taggit.managers import TaggableManager


class DataFile(models.Model):
    name = models.CharField('name',
        help_text='Enter a concise, yet descriptive, name for this data file record.',
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        help_text='Enter a unique <a href="https://en.wikipedia.org/wiki/' \
                  'Semantic_URL#Slug" target="_blank">slug</a> for this data file.<br>' \
                  '(Prepopulated in the admin page based on the data file name.)',
        unique=True,
    )

    file = FilerFileField(
        help_text='Select/Upload a data file.',
        related_name='%(app_label)s_%(class)s_file',
        unique=True,
    )

    description = models.TextField('description',
        blank=True,
        help_text='Enter a description of this data file.',
    )

    tags = TaggableManager(
        blank=True,
        help_text='Add keyword tags that represent this data file.',
    )

    def file_size_fmt(self, suffix='B'):
        """
        Convert file size to human-readable format
        Based on http://stackoverflow.com/a/1094933/996114
        """
        size = self.file.size
        for unit in ['','K','M','G','T','P','E','Z']:
            if abs(size) < 1024.0:
                return '%.1f %s%s' % (size, unit, suffix)
            size /= 1024.0
        return '%.1f %s%s' % (size, 'Y', suffix)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class DataFileSet(models.Model):
    name = models.CharField('name',
        help_text="Enter a unique name for this Data File Set.<br>" \
                  "This won't be displayed on the site.",
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        help_text='Enter a unique <a href="https://en.wikipedia.org/wiki/' \
                  'Semantic_URL#Slug" target="_blank">slug</a> for this data file set.<br>' \
                  '(Prepopulated in the admin page based on the data file set name.)',
        unique=True,
    )

    label = models.CharField('label',
        default='Data',
        help_text='Enter a label for this Data File Set.<br>' \
                  'This will be the heading displayed above the data files.',
        max_length=255,
    )

    description = models.TextField('description',
        blank=True,
        help_text='Enter a description of this data set.',
    )

    image = FilerImageField(
        blank=True,
        null=True,
        help_text='Select/Upload a representative image for this data set.',
        related_name='%(app_label)s_%(class)s_image',
    )

    data_files = models.ManyToManyField(DataFile)

    pagination = models.PositiveIntegerField('files / page',
        default=10,
        help_text="How many data files should be displayed per page? " \
                  "To show all at once, enter '0'.",
    )

    max_words_file_description = models.PositiveIntegerField('max words',
        default=40,
        help_text='Enter the maximum # of words to display for a data file description.<br>' \
                  'Truncated descriptions will have a button for displaying more info.',
    )

    word_buffer_file_description = models.PositiveIntegerField('word buffer',
        default=10,
        help_text="The 'word buffer' prevents descriptions from being truncated " \
                  "if they are only slightly over the 'max words' cutoff.<br>" \
                  "For example, with 'max words' of 40 and a 'word buffer' of 10, " \
                  "descriptions longer than 50 words will be truncated to 40.",
    )

    searchable = models.BooleanField('searchable?',
        default=True,
        help_text='Enable data file search and keyword filter.'
    )

    tags = TaggableManager(
        blank=True,
        help_text='Add keyword tags that represent this data set.',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class DataFileSetPlugin(CMSPlugin):
    data_file_set = models.ForeignKey('cms_lab_data.DataFileSet')

    def __str__(self):
        return self.data_file_set.name
