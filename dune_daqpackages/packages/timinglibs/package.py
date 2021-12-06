# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Timinglibs(CMakePackage):
    """Timing control and monitoring"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/timinglibs/"
    url      = "https://codeload.github.com/DUNE-DAQ/timinglibs/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("1.2.0", sha256='3e2bcde77e8104318443f2eebf59058555fd4aeec3a211d4d39eb105009e89d8', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/timinglibs/legacy.tar.gz/dunedaq-v2.8.0")
    version("1.4.0", sha256='aa2a9ffc42d476b331d488ceb342c638ac9b465cf3a8531e26e9f0696cb92936', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/timinglibs/legacy.tar.gz/dunedaq-v2.8.2")

    depends_on("daq-cmake")
    depends_on("ers")
    depends_on("timing")
    depends_on("dfmessages@2.2.0", when="@1.2.0")
    depends_on("dfmessages@2.2.1", when="@1.4.0:")
    depends_on("uhal")
    depends_on("logging")
    depends_on("appfwk")
    depends_on("rcif")
    depends_on("opmonlib")
    depends_on("cmdlib")
    depends_on("ers")
    
    depends_on("nlohmann-json")
    depends_on("pugixml")
    depends_on("py-moo", type='build')

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

