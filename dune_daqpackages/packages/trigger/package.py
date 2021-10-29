# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Trigger(CMakePackage):
    """Modules that make up the DUNE FD DAQ trigger system"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/trigger/"
    url      = "https://codeload.github.com/DUNE-DAQ/trigger/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='1d0e03e377ca975f5f9889109abe3d32acd83c980e80227f3d687f3730387995', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/trigger/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("triggeralgs")
    depends_on("timinglibs")
    depends_on("py-moo", type='build')

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

