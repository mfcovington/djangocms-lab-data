from django.db import models

from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from taggit.managers import TaggableManager


class DataFile(models.Model):
    name = models.CharField('name',
        help_text='Enter a concise, yet descriptive, name for this data file record.',
        max_length=255,
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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class DataFileSet(models.Model):
    name = models.CharField('name',
        help_text='Enter a concise, yet descriptive, name for this data set.',
        max_length=255,
        unique=True,
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

    tags = TaggableManager(
        blank=True,
        help_text='Add keyword tags that represent this data set.',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)