# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

project_url = 'https://github.com/steinheselmans/sphinx-openscad-extension'

requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-openscad',
    version='0.1',
    url=project_url,
    download_url=project_url + '/archive/v0.1.tar.gz',
    license='MIT license',
    author='Stein Heselmans',
    author_email='stein.heselmans@gmail.com',
    description='Sphinx openscad extension',
    long_description=open("README.rst").read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Sphinx :: Extension',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(exclude=['tests', 'example']),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
    keywords = ['openscad',
                'cad',
            ]
)
