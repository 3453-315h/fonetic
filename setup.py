import os
import re
import codecs

from setuptools import find_packages, setup


def abs_path(*relative_path_parts):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        *relative_path_parts)


name = 'fonetic'

with codecs.open(abs_path(name, '__init__.py'), 'r', 'utf-8') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'.*?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

setup(
    name=name,
    version=version,
    url='https://github.com/s0md3v/fonetic',
    download_url='https://github.com/s0md3v/fonetic/tarball/master',
    author='Somdev Sangwan',
    author_email='s0md3v@gmail.com',
    description='Assess pronouncibility of text',
    keywords='fonetic, linguistic, entropy, spell check',
    packages=find_packages(),
    python_requires='>=2',
    py_modules=['fonetic'],
    data_files=[('', ['LICENSE'])],
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])
