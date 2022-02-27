from setuptools import setup, find_packages

from LegadoParser2 import __version__

install_requires = []

with open('requirements.txt', 'r') as f:
    t = f.read()
    install_requires = list(filter(None, t.split('\n')))

extra_ocr = ['fonttools~=4.29.1', 'cnocr~=2.1.0']

extras_require = {'ocr': extra_ocr}

package_data = {'': ['*.dll', '*.pyd', '*.js']}

setup(
    name='LegadoParser',
    version=__version__,

    url='https://github.com/821938089/LegadoParser',
    author='Horis',

    packages=find_packages(include=['LegadoParser2', 'LegadoParser2.*']),

    install_requires=install_requires,

    extras_require=extras_require,

    package_data=package_data
)