#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
import io

from setuptools import setup

#
__author__ = "Hunor Portik"
__copyright__ = f"Copyright (C) 2021 {__author__}"
__license__ = "MIT License"
__version__ = "1.0"


def read_file(file_path: str) -> str:
    with io.open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


readme = read_file('README.md')
install_requires = []
tests_require = []
extras = {
    'test': tests_require,
}

setup(
    name='mainmodulename',
    version=__version__,
    description=('To show off how a cool project looks like.'),
    long_description=readme,
    author=__author__,
    author_email='@portikCoder',
    url='https://bitbucket.platform.dev.sdt.ericsson.se/projects/CEM/repos/cem-input-data-validator/browse',
    packages=[
        'mainmodulename',
    ],
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'mainmodulename = mainmodulename.main:main',
        ]
    },
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    keywords=(
        'take this, python project base, python plugin base'
    ),
)
