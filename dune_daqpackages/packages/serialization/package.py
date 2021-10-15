# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Serialization(CMakePackage):
    """Utilities for C++ object serialization/deserialization"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/serialization/"
    url      = "https://codeload.github.com/DUNE-DAQ/serialization/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='008cf64f9ede712cca240908dd181e28008b510f2042a343f0079ae2c7640afe', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/serialization/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("appfwk")
    depends_on("logging")

    depends_on("py-moo")

    depends_on("msgpack-c")
    depends_on("nlohmann-json")

    def setup_run_environment(self, env):
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
