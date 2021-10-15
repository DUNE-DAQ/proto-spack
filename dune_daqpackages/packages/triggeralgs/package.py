# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Triggeralgs(CMakePackage):
    """Trigger algorithms"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/triggeralgs/"
    url      = "https://codeload.github.com/DUNE-DAQ/triggeralgs/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='51fbdbc71b77f1bfc0c80d7eb766b9b58bbf55186997cdd5d34cf859e02c31da', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/triggeralgs/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("nlohmann-json")
    depends_on("trace")

    def setup_run_environment(self, env):
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

