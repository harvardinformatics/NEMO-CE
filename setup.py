from setuptools import find_namespace_packages, setup

setup(
    name="NEMO",
    version="6.1.0.dev",
    python_requires=">=3.8, <4",
    packages=find_namespace_packages(exclude=["resources", "resources.*", "build", "build.*"]),
    include_package_data=True,
    url="https://github.com/usnistgov/NEMO",
    license="NIST-Software",
    author="Center for Nanoscale Science and Technology",
    author_email="CNSTapplications@nist.gov",
    description="NEMO is a laboratory logistics web application. Use it to schedule reservations, control tool access, track maintenance issues, and more.",
    long_description="Find out more about NEMO on the GitHub project page https://github.com/usnistgov/NEMO",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "License :: Public Domain",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Framework :: Django :: 3.2",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    install_requires=[
        "cryptography==42.0.8",
        "Django==4.2.11",
        "django-auditlog==3.0.0",
        "django-filter==23.5",
        "django-mptt==0.14.0",
        "djangorestframework==3.15.1",
        "drf-excel==2.4.0",
        "drf-flex-fields==1.0.2",
        "ldap3==2.9.1",
        "Pillow==10.3.0",
        "pymodbus==3.3.2",
        "python-dateutil==2.9.0",
        "requests==2.32.3",
    ],
    extras_require={"dev-tools": ["pre-commit", "djlint", "black"]},
    entry_points={
        "console_scripts": ["nemo=NEMO.provisioning:entry_point"],
    },
)
