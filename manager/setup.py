import os
from setuptools import find_packages, setup
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
README = readme.read()
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
	name='django-repository-manager',
	version='0.1',
	packages=find_packages(),
	include_package_data=True,
	license='CC BY-NC 4.0',
	description='A simple Django app to institutional repository',
	long_description=README,
	url='http://www.example.com/',
	author='Ciano Saraiva',
	author_email='saraiva.ufc@gmail.com',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Framework :: Django :: 1.8', # replace "X.Y" as appropriate
		'Intended Audience :: Developers',
		'License :: OSI Approved :: CC BY-NC 4.0', # example license
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		# Replace these appropriately if you are stuck on Python 2.
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
)