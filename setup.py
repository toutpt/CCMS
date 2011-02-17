from setuptools import setup, find_packages
import os

version = '1.0b6'

setup(name='CCMS',
      version=version,
      description="Base gallery product for plone with picasa and flickr support by Makina Corpus",
      long_description="",
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Django",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Nabil BABACHE',
      author_email='',
      url='https://github.com/bnabilos/CCMS',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cms'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
	  'Django'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
