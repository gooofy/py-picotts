#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name                 ='py-picotts',
      version              ='0.1.2',
      description          ='Python interface for SVOX Pico TTS pico2wave',
      long_description     = open('README.md').read(),
      author               = 'Guenter Bartsch',
      author_email         = 'guenter@zamia.org',
      maintainer           = 'Guenter Bartsch',
      maintainer_email     = 'guenter@zamia.org',
      url                  = 'https://github.com/gooofy/py-picotts',
      classifiers          = [
                              'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
                              'Topic :: Multimedia :: Sound/Audio :: Speech',
                              'Operating System :: POSIX :: Linux',
                              'License :: OSI Approved :: Apache Software License',
                              'Programming Language :: Python :: 2',
                              'Programming Language :: Python :: 2.7',
                              'Programming Language :: Python :: 3',
                              'Programming Language :: Python :: 3.4',
                             ],
      platforms            = 'Linux',
      license              = 'Apache',
      package_dir          = {'picotts': 'picotts'},
      packages             = ['picotts']
      )

