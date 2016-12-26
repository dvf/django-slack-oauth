import os

from setuptools import setup


KEYWORDS = ["django", "slack", "oauth", "integration"]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
INSTALL_REQUIRES = [
    'Django>=1.8',
    'requests',
    'jsonfield==1.0.3'
]

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-slack-integration",
    description="Lightweight OAuth integration with Slack for your Django Projects.",
    license="MIT Licence",
    url="https://github.com/vanflymen/django-slack-oauth",
    download_url='https://github.com/vanflymen/django-slack-oauth/tarball/1.0',
    version="1.0",
    author="Daniel van Flymen",
    author_email="vanflymen@gmail.com",
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=[
        'django_slack_oauth',
        'django_slack_oauth.migrations',
    ],
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
)

