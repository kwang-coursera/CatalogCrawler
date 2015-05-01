from setuptools import setup

setup(name='CatalogCrawler',
      version='0.21',
      description='Tools to crawl course catalogs',
      url='',
      author='Ke Wang',
      author_email='kewang55@gmail.com',
      license='MIT',
      packages=['CatalogCrawler'],
      install_requires=[
          'requests',
          'pandas',
          'lxml'
      ],
      zip_safe=False
      )
