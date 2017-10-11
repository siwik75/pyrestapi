# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


github_url = ("https://github.com/siwik75/simon.siwik@gmail.com/"
              "HerokuPyRestApi")

try:
    with open('README.md') as f:
        readme = f.read()
except:
    readme = "Please see the README.md file at {}.".format(github_url)

setup(
    name='pyrestapi',
    version='0.1b',
    description='First project using Python and Flask to start up a REST Api server on SQLlite and using Heroku for deployment',
    long_description=readme,
    author='Simone Paganini',
    author_email='spaganini@salesforce.com',
    url=github_url,
    license='License :: Other/Proprietary License',
    packages=find_packages(exclude=('tests', 'docs'))
)
