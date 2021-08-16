# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cetmodules(CMakePackage):
    """CMake glue modules and scripts required by packages originating at
    Fermilab and associated experiments and other collaborations.
    """


    homepage = 'https://github.com/FNALssi/cetmodules'
    url = 'https://github.com/FNALssi/cetmodules/archive/refs/tags/2.24.02.tar.gz'

    version('2.24.02', sha256='e2744fd2edaa82c5acd42c369a49217758e90b005a77864eb1a994244811c896')

    depends_on('cmake@3.20.5', type='build')
    depends_on('py-sphinx@4.1.2', type='build')
    depends_on('py-sphinxcontrib-moderncmakedomain@3.19', type='build')
    depends_on('catch2@2.13.4', type='build')
#    depends_on('cmake@3.12:', type='build', when='@1.02.00:')

    def cmake_args(self):

        spec = self.spec

        cmake_args = [
            '-DCMAKE_INSTALL_PREFIX:PATH={0}'.format(spec.prefix)
        ]

        return cmake_args

#    def url_for_version(self, version):
#        url = 'http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/{0}.v{1}.tbz2'
#        return url.format(self.name, version.underscored)
