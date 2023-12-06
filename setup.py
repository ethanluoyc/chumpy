"""
Author(s): Matthew Loper

See LICENCE.txt for licensing and contact information.
"""

from setuptools import setup
from runpy import run_path

def get_version():
    namespace = run_path('chumpy/version.py')
    return namespace['version']

setup(version=get_version())
