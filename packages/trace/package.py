# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install trace
#
# You can edit this file again by typing:
#
#     spack edit trace
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os
from spack.util.environment import EnvironmentModifications

class Trace(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/trace"
    url="https://scisoft.fnal.gov/scisoft/packages/TRACE/v3_16_02/TRACE-3.16.02-sl7-x86_64.tar.bz2"
#    git      = "http://cdcvs.fnal.gov/projects/trace-git"

#    version('stable', branch='stable')
    version('3.16.02')

    patch('install-exec.diff', when='3.15.09')
    patch('install-scripts.diff', when='stable')

    depends_on('cetmodules@1.01.01:', when='3.15.09', type='build')