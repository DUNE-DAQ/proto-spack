# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class DaqCmake(CMakePackage):
    """CMake support for DUNE-DAQ packages"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/daq-cmake/"
    url      = "https://github.com/DUNE-DAQ/daq-cmake"

    maintainers = ["jcfreeman2"]

    version('issue161', branch='johnfreeman/daq-buildtools_issue161', git=url)
