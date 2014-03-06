from setuptools import setup, find_packages
import os

version = '0.1.0'

install_requires = ['setuptools',
                    'Plone',
                    'zope.component',
                    'zope.annotation',
                    'plone.app.registry']

tests_require = ['plone.app.testing', ]

setup(name='collective.portletcollapser',
      version=version,
      description="A js plugin that allows to add expand/collapse behaviour to a set of portlets",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Development Status :: 3 - Alpha",
        ],
      keywords='portlet jquery javascript plone',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='https://github.com/RedTurtle/collective.portletcollapser',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
