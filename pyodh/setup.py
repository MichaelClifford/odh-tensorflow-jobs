import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


def get_install_requires():
    with open('requirements.txt', 'r') as requirements_file:
        # TODO: respect hashes in requirements.txt file
        res = requirements_file.readlines()
        return [req.split(' ', maxsplit=1)[0] for req in res if req]


def get_test_requires():
  if os.path.exists('requirements-test.txt'):
    with open('requirements-test.txt', 'r') as requirements_file:
        res = requirements_file.readlines()
        return [req.split(' ', maxsplit=1)[0] for req in res if req]
  else:
    return []


class Test(TestCommand):
    user_options = [
        ('pytest-args=', 'a', "Arguments to pass into py.test")
    ]

    def initialize_options(self):
        super().initialize_options()
        self.pytest_args = ['--timeout=2', '--cov=./thoth', '--capture=no', '--verbose']

    def finalize_options(self):
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.pytest_args))


setup(
    name='pyodh',
    version="0.0.1",
    description='',
    long_description='',
    author='Vaclav Pavlin',
    author_email='vasek@redhat.com',
    license='GPLv3+',
    packages=[
        'pyodh'
    ],
    zip_safe=False,
    install_requires=get_install_requires(),
    tests_require=get_test_requires(),
    cmdclass={'test': Test},
)