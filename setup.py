""" A panda-3d-isometric-demo Python project
"""

import codecs

import setuptools

def readme():
    """ Load repository README.rst
    """
    with codecs.open('README.rst') as file_handle:
        return file_handle.read()

setuptools.setup(
    name='panda-3d-isometric-demo',

    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1.dev1',

    description='A panda-3d-isometric-demo Python project',
    long_description=readme(),

    url='https://github.com/thorsummoner/panda-3d-isometric-demoproject',

    author='Dylan Grafmyre',
    author_email='thorsummoner0@gmail.com',

    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords=' '.join([
        'panda-3d-isometric-demo',
    ]),

    packages=[
        'p3id'
    ],

    install_requires=[
        'panda3d',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'panda-3d-isometric-demo': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'panda-3d-isometric-demo=p3id.__main__:main',
        ],
    },
)
