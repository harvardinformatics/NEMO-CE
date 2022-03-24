from setuptools import find_packages, setup

setup(
	name='NEMO',
	version='4.0.0.dev',
	python_requires='>=3.7',
	packages=find_packages(exclude=['NEMO.tests','NEMO.tests.*']),
	include_package_data=True,
	url='https://github.com/usnistgov/NEMO',
	license='Public domain',
	author='Center for Nanoscale Science and Technology',
	author_email='CNSTapplications@nist.gov',
	description='NEMO is a laboratory logistics web application. Use it to schedule reservations, control tool access, track maintenance issues, and more.',
	long_description='Find out more about NEMO on the GitHub project page https://github.com/usnistgov/NEMO',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Science/Research',
		'Intended Audience :: System Administrators',
		'License :: Public Domain',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.6',
	],
	install_requires=[
		'cryptography==36.0.1',
		'Django==3.2.12',
		'django-filter==21.1',
		'drf-excel==2.1.0',
		'djangorestframework==3.13.1',
		'drf-flex-fields==0.9.7',
		'ldap3==2.9.1',
		'python-dateutil==2.8.2',
		'requests==2.27.1',
		'Pillow==9.0.1',
		'django-mptt==0.13.4',
	],
	entry_points={
		'console_scripts': ['nemo=NEMO.provisioning:entry_point'],
	},
)
