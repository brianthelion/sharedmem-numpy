#!/usr/bin/env python

# Can use this file via setup.py build_ext --inplace
# during development
#from setuptools import setup  # problems with cython, see setupegg.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import sys

## configuration

import numpy as np

print "sys.platform:", sys.platform

if sys.platform == 'win32':

    winshared =  Extension("npshm.sharedmemory_win", ["npshm/sharedmemory_win.pyx", "npshm/ntqueryobject.c"],
                           include_dirs=[np.get_include()])



    ext_modules = [winshared]

else: #if sys.platform == 'linux2' # or 'darwin'
    lib_dirs = [r'/usr/local/lib', r'.']
    libs = ['m']

    unixshared =  Extension("npshm.sharedmemory_sysv",
                            ["npshm/sharedmemory_sysv.pyx"],
                            include_dirs=[np.get_include()],
                           library_dirs=lib_dirs,
                           libraries=libs)
    ext_modules = [unixshared]


setup(
    author="Sturla Molden",
    name="npshm",
    version="",
    license='scipy license (http://scipy.org)', 
    description="numpy-sharedmem  easy to use shared memory implementation for numpy to make it easy to share memory in an array across processes and threads.",
    url='',
    classifiers=[
        "Development Status :: 3 - alpha, research",
        "Intended Audience :: Scientific programmers",
        "License :: scipy",
        "Operating System :: unix, windows"],
    packages=["npshm"],
#    zip_safe=False, # because of ext module
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,

)
