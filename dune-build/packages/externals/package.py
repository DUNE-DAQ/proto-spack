# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Externals(BundlePackage):
    """A dummy package meant to pull in packages needed by DUNE DAQ developers"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/latest/"

    version("dunedaq-v2.8.2")

    depends_on("devtools@dunedaq-v2.8.2", when="@dunedaq-v2.8.2")

    depends_on("boost@1.73.0 +context+container cxxstd=17", when="@dunedaq-v2.8.2")
    depends_on('folly cxxstd=17', when="@dunedaq-v2.8.2")    
    depends_on("cetlib@3.13.04", when="@dunedaq-v2.8.2")
    depends_on("trace@3.16.02", when="@dunedaq-v2.8.2")

    depends_on('nlohmann-json@3.9.0', when="@dunedaq-v2.8.2")
    depends_on('pistache@dunedaq-v2.8.0', when="@dunedaq-v2.8.2") # Same version for 2.8.0 and 2.8.2
    depends_on('highfive@2.3.1', when="@dunedaq-v2.8.2")
    depends_on('libzmq@4.3.1', when="@dunedaq-v2.8.2")
    depends_on('cppzmq@4.3.0', when="@dunedaq-v2.8.2")
    depends_on('msgpack-c@3.3.0', when="@dunedaq-v2.8.2")
    depends_on('felix-software@dunedaq-v2.8.0', when="@dunedaq-v2.8.2") # Same version for 2.8.0 and 2.8.2
    depends_on('py-pybind11@2.6.2', when="@dunedaq-v2.8.2")
    depends_on('uhal@2.8.1', when="@dunedaq-v2.8.2")
    depends_on('cpr@1.5.2', when="@dunedaq-v2.8.2")
    depends_on('librdkafka@1.7.0', when="@dunedaq-v2.8.2")
    depends_on('protobuf@3.14.0', when="@dunedaq-v2.8.2")

