# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Cmdlib(CMakePackage):
    """Interfaces for commanded objects"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/latest/packages/cmdlib/"
    
    maintainers = ['jcfreeman2']

    version('dunedaq-v2.8.0', sha256='049a6de55b4a53a9c101a268a521cd0c5086acadab8e490d29c8918de3d17723', extension='tar.gz', url="https://codeload.github.com/DUNE-DAQ/cmdlib/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on('daq-cmake')
    depends_on('nlohmann-json')
    depends_on('cetlib')
    depends_on('logging')

    depends_on('py-moo')

    def setup_run_environment(self, env):
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
