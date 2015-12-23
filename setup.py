#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='monarch',
      version='0.1.1',
      packages = find_packages(),
      # metadata for upload to PyPI
      author='peppertap',
      description='Monarch is a throttle for task/jobs like push notification, sms or emails.',
      author_email='backend+monarch@peppertap.com',
      license = "MIT",
      keywords = "monarch, dnd, DoNotDisturb",
      url='https://github.com/Peppertap/monarch',
      test_suite='nose.collector',
      tests_require=['nose', 'ludibrio'],
      install_requires=[
          'redis',
      ],
)
