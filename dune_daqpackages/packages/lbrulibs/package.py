# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Lbrulibs(CMakePackage):
    """DAQ modules, utilities, and scripts for DUNE-ND Upstream DAQ Low Bandwidth Readout Unit"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/lbrulibs/"
    url      = "https://codeload.github.com/DUNE-DAQ/lbrulibs/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("1.0.3", sha256='365e361c8736aa365d31e036f6cf7b8b0fc0c0dc04abf3e62bb83838a7afa65b', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/lbrulibs/legacy.tar.gz/dunedaq-v2.8.0")
    version("1.0.5", sha256='70171acdacd6e4fedde5b61e0464433d02948b552445205ebe3f60fd22d66eec', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/lbrulibs/legacy.tar.gz/dunedaq-v2.8.2")

    depends_on("daq-cmake")
    depends_on("readout")
    depends_on("ipm")
    depends_on("appfwk")
    depends_on("logging")
    depends_on("dataformats", when="@1.0.3")
    depends_on("detdataformats", when="@1.0.5:")
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

