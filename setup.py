import os

from setuptools import find_packages
from setuptools import setup

version = '2.11.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = read('README.rst')

setup(
    name='js.momentjs',
    version=version,
    description="Fanstatic packaging of Angular UI Bootstrap",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Mikhael Malkov',
    author_email='viruzzz.soft@gmail.com',
    url='https://github.com/hitsl/js.momentjs',
    license='MIT',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'momentjs = js.momentjs:library',
            ],
        },
    )
