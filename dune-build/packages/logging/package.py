# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

class Logging(CMakePackage):
    """Contains the functions DUNE DAQ packages use to output text"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/latest/packages/logging/"
    url      = "https://codeload.github.com/DUNE-DAQ/logging/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ['jcfreeman2']

    version('dunedaq-v2.8.0', sha256='fdf0e8a6ca4f223c584e18af25fad146401d1b6a2545cc62c6b1787e92d271f5', extension='tar.gz')

    depends_on('daq-cmake')
    depends_on('trace')
    depends_on('ers')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
