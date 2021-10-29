# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Dqm(CMakePackage):
    """Software and tools for data monitoring"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/dqm/"
    url      = "https://codeload.github.com/DUNE-DAQ/dqm/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='80e872d0e55130f9f560f19730e0934f2c6d211eab9af5112575717520a7cc32', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/dqm/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("readout")
    depends_on("appfwk")
    depends_on("opmonlib")
    depends_on("dataformats")
    depends_on("timinglibs")
    depends_on("librdkafka")
    depends_on("py-moo", type='build')
    depends_on("cyrus-sasl")

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

