# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Timing(CMakePackage):
    """C++ interface to the timing firmware"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/timing/"
    url      = "https://codeload.github.com/DUNE-DAQ/timing/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='17ef87db84ff85fecae32b01ceb755a5e43af46a883ed6fab3653e1cfaa6bc09', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/timing/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on('logging')
    depends_on('opmonlib')
    depends_on('boost')
    depends_on('py-pybind11')
    depends_on('nlohmann-json')
    depends_on('uhal')
    depends_on("py-moo")

    def setup_run_environment(self, env):
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

