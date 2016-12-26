# -*- coding: utf-8 -*-

import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-slack-integration',
    version='0.9',
    packages=[
        'django_slack_oauth',
        'django_slack_oauth.migrations',
    ],
    include_package_data=True,
    license='MIT License',
    description='Lightweight OAuth integration with Slack for your Django Projects',
    long_description=README,
    author='Daniel van Flymen',
    author_email='vanflymen@gmail.com',
    url='https://github.com/vanflymen/django-slack-oauth',
    download_url='https://github.com/vanflymen/django-slack-oauth/tarball/0.9',
    keywords=['django', 'slack', 'oauth'],
    install_requires=[
        'Django>=1.8',
        'requests',
        'jsonfield==1.0.3',
    ],
)
