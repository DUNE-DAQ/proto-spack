# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import env
import os

class Listrev(CMakePackage):
    """Educational example of DAQ modules for new developers"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/listrev/"
    url      = "https://codeload.github.com/DUNE-DAQ/listrev/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='31250d8f002ce96ad90cd9cb18ab8bf9053abd57f591c019cd6b7c580ecd9236', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/listrev/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("appfwk")
    depends_on("daq-cmake")
    depends_on("rcif")
    depends_on("opmonlib")

    depends_on("py-moo", type='build')

    def setup_run_environment(self, env):
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
