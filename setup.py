import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


# allow setup.py to be run from any path
os.chdir(
    os.path.normpath(
        os.path.join(
            os.path.abspath(__file__),
            os.pardir
        )
    )
)


setup(
    name='djangologusername',
    version='0.0.1',
    packages=find_packages(),
    lincense='MIT',
    description='Django helper app for logging username.',
    long_description=README,
    url='https://github.com/mmiyajima2/django-logusername',
    author='Masafumi Miyajima',
    author_email='mmiyajima2@gmail.com',
    install_requires=[
        'django',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
