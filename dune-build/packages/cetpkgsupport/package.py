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

    for build_type in ["Debug", "Release", "RelWithDebInfo"]:
        depends_on(f'cmake@3.20.5 build_type={build_type}', when=f'build_type={build_type}')
