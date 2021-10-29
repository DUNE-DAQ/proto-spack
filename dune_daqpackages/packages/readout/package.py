# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Readout(CMakePackage):
    """Upstream DAQ readout, DAQ modules, CCM interface implementations"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/readout/"
    url      = "https://codeload.github.com/DUNE-DAQ/readout/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='4575251e054f56fd6c48280e3419cc92db436a681f6e30487126eaae42e84834', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/readout/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("trigger")
    depends_on("timinglibs")
    depends_on("triggeralgs")
    depends_on("dfmessages")
    depends_on("appfwk")
    depends_on("folly")
    depends_on("dataformats")
    depends_on("opmonlib")
    depends_on("logging")

    depends_on('boost+context+container cxxstd=17')
    depends_on("py-moo", type='build')



    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

