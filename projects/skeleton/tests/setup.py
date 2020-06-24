try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'Faezeh',
    'url' : 'https://www.linkedin.com/in/faezeh-arab-hassani-11318317b/',
    'download_url' : 'Where to download it',
    'author_email' : 'faezeh@go.com',
    'version' : '0.1',
    'instal_requires' : ['nose'],
}
