# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Nwqueueadapters(CMakePackage):
    """DAQ modules that connect appfwk queues to IPM network connections"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/nwqueueadapters/"
    url      = "https://codeload.github.com/DUNE-DAQ/nwqueueadapters/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("1.4.0", sha256='76298a304ac50b035bbab4ffc011f91a81037123740a69a0a795e015857298aa', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/nwqueueadapters/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("daq-cmake")
    depends_on("appfwk")
    depends_on("logging")
    depends_on("ipm")
    depends_on("serialization")
    depends_on("opmonlib")
    depends_on("py-moo", type='build')

    depends_on("nlohmann-json")

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
        env.prepend_path("PYTHONPATH", self.prefix.lib + "64/python")
