import os
import sys
from setuptools import setup

if sys.version_info < (3, 2):
    print("Sorry, djangocms-lab-data currently requires Python 3.2+.")
    sys.exit(1)

# From: https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    "Django>=1.7.7,<1.8",
    "django-cms>=3.0",
    "django-filer>=0.9.10",
    "django-taggit>=0.14.0",
    "django-taggit-helpers>=0.1.1",
]

setup(
    name='djangocms-lab-data',
    version='0.0.0',
    packages=['cms_lab_data'],
    include_package_data=True,
    license='BSD License',
    description='A Django app for organizing data files and sets of data files within a Django site with django CMS-specific features',
    long_description=(read('README.rst'))
    url='https://github.com/mfcovington/djangocms-lab-data',
    author='Michael F. Covington',
    author_email='mfcovington@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
)
