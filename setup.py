#!/usr/bin/env python

from setuptools import setup, find_packages

EXCLUDED = ['*.tests', '*.tests.*', 'tests.*', 'tests']

setup(name                 ='py-picotts',
      version              ='0.1.0',
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
                              'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                              'Programming Language :: Python :: 2',
                              'Programming Language :: Python :: 2.7',
                              'Programming Language :: Python :: 3',
                              'Programming Language :: Python :: 3.4',
                             ],
      platforms            = 'Linux',
      license              = 'LGPLv3',
      package_dir          = {'picotts': 'picotts'},
      test_suite           = 'tests',
      packages             = find_packages('.', EXCLUDED),
      )

