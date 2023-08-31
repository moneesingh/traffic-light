import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "traffic-light-simulator",
    version = "0.0.1",
    author = "Monee Kumar",
    description = ("A simple traffic light simulator"),
    long_description=read('README.md')
    author_email = 'moneesingh@yahoo.com',
    url = 'https://github.com/moneesingh/traffic-light', 
    download_url = 'https://github.com/moneesingh/traffic-light-simulator/archive/0.1.tar.gz', 
    keywords = ['testing', 'example'], 
    classifiers = [],
    entry_points = {
        'console_scripts': ['traffic-light-simulator=main:main'],
    },
)