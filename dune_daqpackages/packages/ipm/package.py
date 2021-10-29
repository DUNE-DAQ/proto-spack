# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Ipm(CMakePackage):
    """Message passing between processes"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/ipm/"
    url      = "https://codeload.github.com/DUNE-DAQ/ipm/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("2.2.0", sha256='4c907785d5edfc9108a990653be4b991b25db2e594c6a31439cf5a1631a24c90', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/ipm/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("daq-cmake")
    depends_on("appfwk")
    depends_on("logging")
    depends_on("ers")
    depends_on("cetlib")

    depends_on("cppzmq")
    depends_on("nlohmann-json")

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

