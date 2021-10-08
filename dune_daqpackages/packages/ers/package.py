# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Ers(CMakePackage):
    """A fork of the ATLAS Error Reporting System"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/latest/packages/ers/"
    url      = "https://codeload.github.com/DUNE-DAQ/ers/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ['jcfreeman2']

    version('dunedaq-v2.8.0', sha256='41679c231ffb6a7be83d4d9662c563ff1824e46bf0095e7fa93c5a86fcd3639a', extension='tar.gz')

    depends_on('daq-cmake')
    depends_on('boost')
    depends_on('py-pybind11')

    def setup_run_environment(self, env):
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

