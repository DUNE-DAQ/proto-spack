# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Dfmodules(CMakePackage):
    """Dataflow Applications"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/dfmodules/"
    url      = "https://codeload.github.com/DUNE-DAQ/dfmodules/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("2.2.1", sha256='c62c967508b0b24101eb529be47311ea6c0a26efa55f3f5a59a4942acff073a4', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/dfmodules/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("daq-cmake")
    depends_on("readout")
    depends_on("trigger")
    depends_on("triggeralgs")
    depends_on("timinglibs")
    depends_on("dfmessages")
    depends_on("serialization")
    depends_on("appfwk")
    depends_on("opmonlib")
    depends_on("logging")
    depends_on("py-moo", type='build')

    depends_on("highfive@2.2.2")
    depends_on("boost+context+container cxxstd=17")

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

