# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Minidaqapp(CMakePackage):
    """Application to read out Felix data and store it in HDF5 files on disk"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/minidaqapp/"
    url      = "https://codeload.github.com/DUNE-DAQ/minidaqapp/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("4.0.0", sha256='1a3f5585ffa794634eaf68f3481510a912dbfc324f0a6706b74e71514330ebd2', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/minidaqapp/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("daq-cmake")
    depends_on("py-moo", type='build')

    # DBT_DEBUG is used by daq-cmake to set compiler options 
    def cmake_args(self): 
        if str(self.spec.variants['build_type']) == "build_type=Debug": 
            return ["-DDBT_DEBUG=true"] 
        else: 
            return ["-DDBT_DEBUG=false"] 

    def setup_run_environment(self, env):
        env.set(self.__module__.split(".")[-1].upper().replace("-", "_") + "_SHARE", self.prefix + "/share" )
        env.prepend_path('DUNEDAQ_SHARE_PATH', self.prefix + "/share")
        env.prepend_path('PYTHONPATH', self.prefix.lib + "64/python")

