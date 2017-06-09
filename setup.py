# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

project_url = 'https://github.com/steinheselmans/sphinx-openscad-extension'
version = '0.1.0'

requires = ['Sphinx>=0.6']

setup(
    name='mlx.openscad',
    version=version,
    url=project_url,
    download_url=project_url + '/tarball/' + version,
    license='MIT license',
    author='Stein Heselmans',
    author_email='teh@melexis.com',
    description='Sphinx openscad extension',
    long_description=open("README.rst").read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(exclude=['tests', 'example']),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['mlx'],
    keywords = [
        'sphinx',
        'openscad',
        'cad',
    ],
)
