import codecs
import os
from setuptools import setup
from yuque_py import __version__

here = os.path.abspath(os.path.dirname(__file__))

readme = codecs.open('README.md', encoding='utf-8').read()
history = codecs.open('HISTORY.md', encoding='utf-8').read()

packages = ["yuque_py", "yuque_py.models", "yuque_py.clients", "yuque_py.exceptions"]

requires = [
    "pytest==5.1.1",
    "pytest-cov==2.7.1",
    "requests==2.22.0",
    "requests-mock==1.6.0"
]

setup(
    name="yuque-py",
    version=__version__,
    description="yuque api for python version",
    long_description=u'\n\n'.join([readme, history]),
    long_description_content_type='text/markdown',
    author="Manjusaka",
    author_email="me@manjusaka.me",
    url="https://github.com/Zheaoli/yuque-py",
    packages=packages,
    install_requires=requires,
    include_package_data=True,
    license="MIT License",
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
