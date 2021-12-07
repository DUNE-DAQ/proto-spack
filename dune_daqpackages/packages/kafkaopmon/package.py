# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Kafkaopmon(CMakePackage):
    """Converts JSON objects into Kafka messages"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.2/packages/kafkaopmon/"
    url      = "https://codeload.github.com/DUNE-DAQ/kafkaopmon/legacy.tar.gz/dunedaq-v2.8.2"

    maintainers = ["jcfreeman2"]

    version("1.3.0", sha256='434b0bfa0ceb83f0665f66f5d242a63956b5b81259c4135edd7c84ba198a08c8', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/kafkaopmon/legacy.tar.gz/dunedaq-v2.8.2")

    depends_on("daq-cmake")
    depends_on("opmonlib")
    depends_on("cpr")
    depends_on("curl")
    depends_on("cyrus-sasl")
    depends_on("librdkafka")
    depends_on("ers")
    depends_on("boost")
    depends_on('py-moo', type='build')

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path('DUNEDAQ_SHARE_PATH', self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
        env.prepend_path("PYTHONPATH", self.prefix.lib + "64/python")


