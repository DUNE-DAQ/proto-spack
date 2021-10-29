# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Rcif(CMakePackage):
    """Run Control related"""

    homepage = "https://github.com/DUNE-DAQ/rcif"
    url      = "https://codeload.github.com/DUNE-DAQ/rcif/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("1.1.1", sha256='e69765efe1eeaffe9c44047b48be481c603c632c48ae00c2e444203217b43a63', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/rcif/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("daq-cmake")
    depends_on("cmdlib")
    depends_on("opmonlib")

    depends_on("py-moo", type='build')

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
