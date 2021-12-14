# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Systems(BundlePackage):
    """The DUNE DAQ programming languages"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/latest/"

    version("develop")
    version("dunedaq-v2.8.2")

    # Leaving gcc out until I figure out how best to handle this...
    for ver in ["develop", "dunedaq-v2.8.2"]:
        depends_on("python@3.8.3 +debug", when=f"@{ver}") # +debug is for gdb
