try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': ('command line program that will parse files specified in ~/.logfind'
                    'and return only the names of files that contain strings passed in'
                    'as arguements'),
    'author': 'Diane Wellman',
    'url': 'https://github.com/stringtheory/name',
    'download_url': 'https://github.com/stringtheory/name',
    'author_email': 'dk8654@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'scripts': [],
    'name': 'logfind'
}

set(**config)