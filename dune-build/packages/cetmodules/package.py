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
    url = 'https://github.com/FNALssi/cetmodules/archive/refs/tags/2.25.04.tar.gz'

    version('2.25.04', sha256='c2a8d3496dfd2c0dd4194652e87416f2ad4ff65250976070519e8f8ea33252d8')

    depends_on('cmake@3.20.5', type='build')
    depends_on('py-sphinx@4.1.2', type='build')
    depends_on('py-sphinxcontrib-moderncmakedomain@3.19', type='build')
    depends_on('py-sphinx-rtd-theme@0.5.2', type='build')
    depends_on('catch2@2.13.4', type='build')


    @run_before('cmake')
    def fix_fix_man(self):
        filter_file('exit \$status', 'exit 0', '%s/libexec/fix-man-dirs' % self.stage.source_path)

    def cmake_args(self):

        spec = self.spec

        cmake_args = [
            '-DCMAKE_INSTALL_PREFIX:PATH={0}'.format(spec.prefix)
        ]

        return cmake_args


#    def url_for_version(self, version):
#         if str(version)[0] in "01"    

#    def url_for_version(self, version):
#        url = 'http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/{0}.v{1}.tbz2'
#        return url.format(self.name, version.underscored)
