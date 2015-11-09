# CMS Lab Data

CMS Lab Data is a Django app for organizing data files and sets of data files within a Django site with django CMS-specific features.

<!-- Detailed documentation is in the "docs" directory. -->

## Quick start

- Install `djangocms-lab-data` from GitHub:

    ```sh
    pip install https://github.com/mfcovington/djangocms-lab-data/releases/download/0.0.0/djangocms-lab-data-0.0.0.tar.gz
    ```

- Edit the project's `settings.py` file.

    - Add `cms_lab_data` and its dependencies to your `INSTALLED_APPS` setting:

        ```python
        INSTALLED_APPS = (
            ...
            'taggit',
            'cms_lab_data',
            'easy_thumbnails',
            'filer',
            'mptt',
        )
        ```

    - Add `easy_thumbnail` settings: 

        ```python
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
        ```

- Run `python manage.py makemigrations cms_lab_data` to create the `cms_lab_data` migrations.

- Run `python manage.py migrate` to create the `cms_lab_data` models.

- Start the development server (`python manage.py runserver`) and visit http://127.0.0.1:8000/

- Create a CMS page and insert the `Data Set Plugin` into a placeholder field.

- Create a CMS page and attach the `Data App` under `Advanced Settings` for the page.

- To access `cms_lab_data` pages without using a django CMS AppHook, include URL configurations for `cms_lab_data` and media (if `DEBUG == True`) in your project's `urls.py` file:

    ```python
    ...
    from django.conf import settings

    urlpatterns = [
        ...
        url(r'^data/', include('cms_lab_data.urls', namespace='cms_lab_data')),
        ...
    ]

    if settings.DEBUG:
        urlpatterns += [
            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT})
        ]
    ```

*Version 0.0.0*
