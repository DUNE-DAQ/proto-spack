# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Flxlibs(CMakePackage):
    """DAQ modules, utilities, and scripts for Upstream FELIX Readout Software"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/flxlibs/"
    url      = "https://codeload.github.com/DUNE-DAQ/flxlibs/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='e506aa2b7e10aaaadb3fbac951eb28375ada2c6c65e99ccba5842303c3f59d2d', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/flxlibs/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("appfwk")
    depends_on("logging")
    depends_on("dataformats")
    depends_on("readout")
    depends_on("felix-software")
    depends_on("py-moo")

    def setup_run_environment(self, env):
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

