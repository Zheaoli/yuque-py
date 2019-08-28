import os
from setuptools import setup
from yuque_py import __version__

here = os.path.abspath(os.path.dirname(__file__))

packages = ['yuque_py']

requires = [
    "pytest==5.1.1"
    "pytest-cov==2.7.1"
    "requests==2.22.0"
    "requests-mock==1.6.0",
]

setup(
    name="yuque-py",
    version=__version__,
    decription="yuque api for python version",
    author="Manjusaka",
    author_email="me@manjusaka.me",
    url="https://github.com/Zheaoli/yueque-py",
    packages=packages,
    install_requires=requires,
    include_package_date=True,
    license="MIT License",
    python_requires=">=3.6",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
