******************
djangocms-lab-data
******************

``djangocms-lab-data`` is a Django app for organizing data files and sets of data files within a Django site with django CMS-specific features.

Source code is available on GitHub at `mfcovington/djangocms-lab-data <https://github.com/mfcovington/djangocms-lab-data>`_.


.. contents:: :local:


Installation
============

**GitHub (development branch)**

.. code-block:: sh

    pip install git+http://github.com/mfcovington/djangocms-lab-data.git@develop


Configuration
=============

- `Install django CMS and start a project <http://docs.django-cms.org/en/latest/introduction/install.html>`_, if one doesn't already exist.

  - Unless you use this app as part of `djangocms-lab-site <https://github.com/mfcovington/djangocms-lab-site>`_ or plan to style the app from scratch, you will want to choose the ``Use Twitter Bootstrap Theme`` option (when running ``djangocms``) and then edit the resulting ``templates/base.html``. This will add style that looks like Bootstrap 2. To use Bootstrap 3 styling, remove the following line for the ``bootstrap-theme.min.css`` stylesheet from ``templates/base.html``:

    .. code-block:: python

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.x.x/css/bootstrap-theme.min.css">


- Do the following in ``settings.py``:

  - Add ``cms_lab_data`` and its dependencies to ``INSTALLED_APPS``:

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'taggit',
            'cms_lab_data',
            'easy_thumbnails',
            'filer',
            'mptt',
        )


  - Add ``easy_thumbnail`` settings: 

    .. code-block:: python

        # For easy_thumbnails to support retina displays (recent MacBooks, iOS)
        THUMBNAIL_HIGH_RESOLUTION = True
        THUMBNAIL_QUALITY = 95
        THUMBNAIL_PROCESSORS = (
            'easy_thumbnails.processors.colorspace',
            'easy_thumbnails.processors.autocrop',
            'filer.thumbnail_processors.scale_and_crop_with_subject_location',
            'easy_thumbnails.processors.filters',
        )
        THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
        THUMBNAIL_SUBDIR = 'versions'


Migrations
==========

Create and perform ``cms_lab_data`` migrations:

.. code-block:: sh

    python manage.py makemigrations cms_lab_data
    python manage.py migrate


Usage
=====

- Start the development server:

.. code-block:: sh

    python manage.py runserver


- Visit: ``http://127.0.0.1:8000/``
- Create a CMS page and then:

  - Attach the ``Data App`` under ``Advanced Settings`` for the page, **OR**
  - Insert the ``Data File Set Plugin`` into a placeholder field.


*Version 0.0.0*
