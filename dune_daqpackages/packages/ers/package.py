# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Ers(CMakePackage):
    """A fork of the ATLAS Error Reporting System"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/ers/"
    url      = "https://codeload.github.com/DUNE-DAQ/ers/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("1.1.3", sha256='41679c231ffb6a7be83d4d9662c563ff1824e46bf0095e7fa93c5a86fcd3639a', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/ers/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on('daq-cmake')
    depends_on('boost')

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

