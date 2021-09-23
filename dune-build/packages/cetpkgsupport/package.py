# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os
import sys


class Cetpkgsupport(CMakePackage):
    """CMake glue modules and scripts required by packages originating at
    Fermilab and associated experiments and other collaborations.
    """

    homepage = 'https://gitlab.cern.ch/dune-daq/experimental/externals/cetpkgsupport.git'

    version('master', branch='master', git=homepage)


    depends_on('cmake@3.20.5')

    variant('build_type', default='RelWithDebInfo',
            description='The build type to build',
            values=('Debug', 'Release', 'RelWithDebInfo'))
