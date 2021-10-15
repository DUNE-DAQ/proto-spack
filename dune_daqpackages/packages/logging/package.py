# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Logging(CMakePackage):
    """Contains the functions DUNE DAQ packages use to output text"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/logging/"
    url      = "https://codeload.github.com/DUNE-DAQ/logging/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='fdf0e8a6ca4f223c584e18af25fad146401d1b6a2545cc62c6b1787e92d271f5', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/logging/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on('daq-cmake')
    depends_on('trace')
    depends_on('ers')

    def setup_run_environment(self, env):
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

