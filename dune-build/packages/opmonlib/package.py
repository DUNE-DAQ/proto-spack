# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Opmonlib(CMakePackage):
    """Operational monitoring library"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/latest/packages/opmonlib/"

    maintainers = ['jcfreeman2']

    version('dunedaq-v2.8.0', sha256='5f6e170ee6713b94c1a571233e801ea636f6c5baa61a68ab79ee4eedca0a6934', extension='tar.gz', url="https://codeload.github.com/DUNE-DAQ/opmonlib/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on('daq-cmake')
    depends_on('cetlib')
    depends_on('logging')
    depends_on('nlohmann-json')
