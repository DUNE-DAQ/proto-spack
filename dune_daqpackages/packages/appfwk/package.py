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

    version("dunedaq-v2.8.0", sha256='348e629b9fe86b48690a6895cef46a0c6d67ab5a587514ce128e6dca156cc1cc', extension="tar.gz", url="https://codeload.github.com/DUNE-DAQ/appfwk/legacy.tar.gz/dunedaq-v2.8.0")

    depends_on('daq-cmake')
    depends_on('logging')
    depends_on('cetlib')
    depends_on('folly cxxstd=17')
    depends_on('cmdlib')
    depends_on('rcif')
    depends_on('opmonlib')
    depends_on('nlohmann-json')

    depends_on('py-moo')
    depends_on('boost +context +container cxxstd=17' )
    depends_on('trace')

    def setup_run_environment(self, env):
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")
