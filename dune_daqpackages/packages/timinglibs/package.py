# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Timinglibs(CMakePackage):
    """Timing control and monitoring"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/timinglibs/"
    url      = "https://codeload.github.com/DUNE-DAQ/timinglibs/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='3e2bcde77e8104318443f2eebf59058555fd4aeec3a211d4d39eb105009e89d8', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/timinglibs/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("timing")
    depends_on("dfmessages")
    depends_on("uhal")
    depends_on("logging")
    depends_on("appfwk")
    depends_on("rcif")
    depends_on("opmonlib")
    depends_on("cmdlib")
    depends_on("ers")
    
    depends_on("nlohmann-json")
    depends_on("pugixml")
    depends_on("py-moo")

    def setup_run_environment(self, env):
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

