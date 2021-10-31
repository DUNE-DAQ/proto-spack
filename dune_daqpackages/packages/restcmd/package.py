# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Restcmd(CMakePackage):
    """HTTP REST backend based CommandFacility"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/restcmd/"
    url      = "https://codeload.github.com/DUNE-DAQ/restcmd/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("1.1.3", sha256='840b5a0e115e9699100706b860c7438213917b401f7881ab3f60fe6179b9cfd2', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/restcmd/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("daq-cmake")
    depends_on("cetlib")
    depends_on("logging")
    depends_on("cmdlib")

    depends_on("nlohmann-json")
    depends_on("pistache@dunedaq-v2.8.0", when="@1.1.3")

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
        env.prepend_path("PYTHONPATH", self.prefix.lib + "64/python")
