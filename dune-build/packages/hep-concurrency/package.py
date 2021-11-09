
# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys
from spack import *
from spack.environment import *
import os

#libdir="%s/var/spack/repos/fnal_art/lib" % os.environ["SPACK_ROOT"]
#if not libdir in sys.path:
#    sys.path.append(libdir)


def sanitize_environments(*args):
    for env in args:
        for var in ('PATH', 'CET_PLUGIN_PATH',
                    'LD_LIBRARY_PATH', 'DYLD_LIBRARY_PATH', 'LIBRARY_PATH',
                    'CMAKE_INSTALL_RPATH', 'CMAKE_PREFIX_PATH', 'ROOT_INCLUDE_PATH'):
            env.prune_duplicate_paths(var)
            env.deprioritize_system_paths(var)


class HepConcurrency(CMakePackage):
    """A concurrency library for the art suite."""

    homepage = 'https://gitlab.cern.ch/dune-daq/experimental/externals/hep_concurrency'
    git_base = 'https://gitlab.cern.ch/dune-daq/experimental/externals/hep_concurrency.git'
    url = 'https://gitlab.cern.ch/dune-daq/experimental/externals/hep_concurrency/-/archive/v1_07_04/hep_concurrency-v1_07_04.tar.gz'

    version('1.07.04', tag='v1_07_04', git=git_base, get_full_repo=True)  

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    variant('build_type', default='RelWithDebInfo',
            description='The build type to build',
            values=('Debug', 'Release', 'RelWithDebInfo'))


    patch('hep_concurrency.1.04.01.patch', when='@1.04.01')

    # Build-only dependencies.
    depends_on('cmake@3.20.5 build_type=Debug', when='build_type=Debug', type='build')
    depends_on('cetmodules@2.25.05 build_type=Debug', when='build_type=Debug', type='build')
    depends_on('cetlib-except@1.07.04 build_type=Debug', when='build_type=Debug', type=('build','run'))

    # Build / link dependencies.
    depends_on('cppunit@1.14.0')
    depends_on('catch2@2.13.4')
    depends_on('intel-tbb@2020.3')

    if 'SPACKDEV_GENERATOR' in os.environ:
        generator = os.environ['SPACKDEV_GENERATOR']
        if generator.endswith('Ninja'):
            depends_on('ninja', type='build')

    def cmake_args(self):
        spec = self.spec
        cmake_args = [
            '-DCMAKE_INSTALL_PREFIX:PATH={0}'.format(spec.prefix),
            '-DCMAKE_CXX_STANDARD={0}'.format(self.spec.variants['cxxstd'].value)
        ]
        cmake_args.append('-DCMAKE_PROJECT_VERSION={0}'.format(self.spec.version))
        return cmake_args

    def setup_environment(self, spack_env, run_env):
        # PATH for tests.
        spack_env.prepend_path('PATH', os.path.join(self.build_directory, 'bin'))
        # Cleanup.
        sanitize_environments(spack_env, run_env)
