from setuptools import setup 
import test



setup(
    name='testproj',
    version=test.__version__,
    author='hqman',
    author_email='hqmank@gmail.com',
    description='test setup',
    long_description=open('README.rst').read(),
    license='MIT',
    packages=['test'],
  
    entry_points={
        'console_scripts':[
        'testproj=test.cli:main',
        'hello=test.cli:hello'

        ],
    },

    )