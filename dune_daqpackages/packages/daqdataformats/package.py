# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Daqdataformats(CMakePackage):
    """DUNE DAQ data formats"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.2/packages/daqdataformats/"
    url      = "https://codeload.github.com/DUNE-DAQ/daqdataformats/legacy.tar.gz/dunedaq-v2.8.2"

    maintainers = ["jcfreeman2"]

    version("3.2.1", sha256='c5ac6c1df84e59be6fe185e94793e1a9e8d1380b7ce4d848442e2f2fa6e6effb', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/daqdataformats/legacy.tar.gz/dunedaq-v2.8.2")

    depends_on("daq-cmake")
    depends_on('boost' )
    depends_on('py-moo', type='build')

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path('DUNEDAQ_SHARE_PATH', self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
        env.prepend_path("PYTHONPATH", self.prefix.lib + "64/python")


