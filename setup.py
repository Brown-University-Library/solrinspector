import os

from setuptools import setup

REQUIRED = ['mysolr']

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='sorlinspector',
    version='0.1.0',
    description='Inspect solr fields and facets.',
    long_description=read('README.rst'),
    url='http://github.com/Brown-University-Library/solrinspector/',
    license='MIT',
    author='Joseph Rhoads',
    author_email='joseph_rhoads@brown.edu',
    py_modules=['solrinspector'],
    install_requires=REQUIRED,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
