from setuptools import setup, find_packages
from codecs import open

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='matt-daemon',
    version='1.0.0',
    description='A lightweight HTTP daemon for serving static files. With Matt Daemon, there are no surprises. He just serves.',
    long_description=readme,
    url='https://github.com/k3rn31p4nic/matt-daemon',
    author='k3rn31p4nic',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    keywords='http daemon matt matt-daemon httpd server',
    packages=find_packages(),
    python_requires='>=3.5',
    scripts=[ 'matt.py' ],
)
