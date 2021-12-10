# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Dqm(CMakePackage):
    """Software and tools for data monitoring"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/dqm/"
    url =      "https://github.com/DUNE-DAQ/dqm"

    maintainers = ["jcfreeman2"]

    version("develop", branch="develop", git=url)

    version("1.0.0", sha256='80e872d0e55130f9f560f19730e0934f2c6d211eab9af5112575717520a7cc32', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/dqm/legacy.tar.gz/dunedaq-v2.8.0")
    version("1.1.6", sha256='1ca02fe6dcdf9d0ee7e1bda2f8e36e0fdf7786d28c5154c1b224c2cbec0901fa', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/dqm/legacy.tar.gz/dunedaq-v2.8.2")

    depends_on("daq-cmake")
    depends_on("readout")
    depends_on("appfwk")
    depends_on("opmonlib")
    depends_on("dataformats", when="@1.0.0")
    depends_on("daqdataformats", when="@1.1.6:")
    depends_on("detdataformats", when="@1.1.6:")
    depends_on("detchannelmaps", when="@1.1.6:")
    depends_on("highfive", when="@1.1.6:")
    depends_on("ers", when="@1.1.6:")
    depends_on("boost", when="@1.1.6:")
    depends_on("timinglibs")
    depends_on("librdkafka")
    depends_on("py-moo", type='build')
    depends_on("cyrus-sasl")

    # DBT_DEBUG is used by daq-cmake to set compiler options 
    def cmake_args(self): 
        if str(self.spec.variants['build_type']) == "build_type=Debug": 
            return ["-DDBT_DEBUG=true"] 
        else: 
            return ["-DDBT_DEBUG=false"] 

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
        env.prepend_path("PYTHONPATH", self.prefix.lib + "64/python")

