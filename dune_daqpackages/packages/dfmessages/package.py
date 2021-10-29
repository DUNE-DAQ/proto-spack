# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Dfmessages(CMakePackage):
    """Dataflow messages"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/dfmessages/"
    url      = "https://codeload.github.com/DUNE-DAQ/dfmessages/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("2.2.0", sha256='80b6b78e1d36c6db19b623152a37138470e64cf750370483e0820bbaaa607603', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/dfmessages/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("daq-cmake")
    depends_on("nwqueueadapters")
    depends_on("serialization")
    depends_on("dataformats")

    depends_on('boost +context +container cxxstd=17' )

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

