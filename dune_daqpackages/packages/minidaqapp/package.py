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

    version("dunedaq-v2.8.0", sha256='1a3f5585ffa794634eaf68f3481510a912dbfc324f0a6706b74e71514330ebd2', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/minidaqapp/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("py-moo")
    depends_on("py-pybind11")

    depends_on("py-rich")

    def setup_run_environment(self, env):
        env.prepend_path('PYTHONPATH', self.prefix.lib + "64/python")

