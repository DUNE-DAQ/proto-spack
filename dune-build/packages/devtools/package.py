# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Devtools(BundlePackage):
    """The DUNE DAQ development tools"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/latest/"

    version("dunedaq-v2.8.2")

    depends_on("systems@dunedaq-v2.8.2", when="@dunedaq-v2.8.2")

    depends_on("cmake@3.20.5", when="@dunedaq-v2.8.2")  # Should be 3.17.2, but hep-concurrency needs a newer CMake version
    #depends_on("gdb@9.2", when="@dunedaq-v2.8.2")
    #depends_on("ninja@1.10.0", when="@dunedaq-v2.8.2")
