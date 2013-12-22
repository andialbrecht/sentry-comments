#!/usr/bin/env python

from setuptools import setup, find_packages


# install_requires = [
#     'sentry>=6.0.1,<6.4',
# ]
install_requires = ['sentry>=6.0.1,<6.5']


with open('README.rst') as f:
    LONG_DESCRIPTION = f.read()


setup(
    name='sentry-comments',
    version='0.3.0',
    author='Andi Albrecht',
    author_email='albrecht.andi@gmail.com',
    url='https://github.com/andialbrecht/sentry-comments',
    description='A Sentry extension to add comments to sentry events.',
    long_description=LONG_DESCRIPTION,
    license='BSD',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'sentry.apps': [
            'sentry_comments = sentry_comments',
        ],
        'sentry.plugins': [
            'sentry_comments = sentry_comments.plugin:CommentsPlugin'
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development'
    ],
)
