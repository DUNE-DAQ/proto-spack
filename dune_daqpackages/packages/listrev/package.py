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
    url =      "https://github.com/DUNE-DAQ/listrev"

    maintainers = ["jcfreeman2"]

    version("develop", branch="develop", git=url)

    version("2.1.4", sha256='31250d8f002ce96ad90cd9cb18ab8bf9053abd57f591c019cd6b7c580ecd9236', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/listrev/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("appfwk")
    depends_on("daq-cmake")
    depends_on("rcif")
    depends_on("opmonlib")
    depends_on("logging", when="@develop")
    depends_on("ers", when="@develop")

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
