# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Dataformats(CMakePackage):
    """Raw data reinterpretation utilities"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/dunedaq-v2.8.0/packages/dataformats/"
    url      = "https://codeload.github.com/DUNE-DAQ/dataformats/legacy.tar.gz/dunedaq-v2.8.0"

    maintainers = ["jcfreeman2"]

    version("dunedaq-v2.8.0", sha256='6da3f65d645792bc022468e27bf16d3f9c4f844fa08a5634e5f6cb1f850cf4ef', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/dataformats/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on("ers")
    depends_on("boost")
    depends_on("logging")

    def setup_run_environment(self, env):
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
