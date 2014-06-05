from setuptools import setup, find_packages

setup(
    name='mlogger',
    version='0.1',
    description='Application that helps your models to keep track of all their changes.',
    author='Ruslan Popov',
    author_email='ruslan.popov@gmail.com',
    url='http://github.com/RaD/django-mlogger/tree/master',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)

