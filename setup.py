import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('reports/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('requirements.txt') as f:
    requirements = f.read().split('\n')


setup(
    name='reports',
    author='Seva Gavrilov',
    author_email='gavrilovseva@gmail.com',
    version=version,
    url='https://github.com/trocafone/etls/tree/master/reporter',
    packages=['reports'],
    description='A simple business reporting system',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python'
    ],
    tests_require=['mock==1.3.0'],
    extras_require={
        'drive': ['PyDrive==1.0.1'],
        'test': ['mock==1.3.0'],
        'query': ['SQLAlchemy==1.0.11'],
        'postgres': ['psycopg2==2.6.1']
    },
    scripts=['reporter.py']
)
