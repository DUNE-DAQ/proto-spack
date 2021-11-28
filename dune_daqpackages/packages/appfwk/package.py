# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Appfwk(CMakePackage):
    """Home of daq_application and tools for writing DAQ modules"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/appfwk/"
    url      = "https://codeload.github.com/DUNE-DAQ/appfwk/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("2.3.2", sha256='348e629b9fe86b48690a6895cef46a0c6d67ab5a587514ce128e6dca156cc1cc', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/appfwk/legacy.tar.gz/dunedaq-v2.8.0")
    version('2.3.3', sha256='1683f6e72499c72e7ea2be9469b7d8dead06e5c65780d81ae82e4ce79dadd0fb', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/appfwk/legacy.tar.gz/dunedaq-v2.8.2")

    depends_on('daq-cmake')
    depends_on('logging')
    depends_on('cetlib')
    depends_on('folly cxxstd=17')
    depends_on('ers')
    depends_on('cmdlib')
    depends_on('rcif')
    depends_on('opmonlib')
    depends_on('nlohmann-json')

    depends_on('py-moo', type='build')
    depends_on('boost' )
    depends_on('trace')

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
