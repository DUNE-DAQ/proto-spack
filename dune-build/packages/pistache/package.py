# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Pistache(CMakePackage):
    """An elegant C++ REST framework."""

    homepage = "http://pistache.io"
    url      = "https://github.com/oktal/pistache/archive/v0.0.0.tar.gz"
    git      = "https://github.com/oktal/pistache.git"

    maintainers = ['jcfreeman2']

    version('master', branch='master')
    depends_on('openssl')
    depends_on('libpthread-stubs')

    def patch(self):
        copy(join_path(os.path.dirname(__file__),
             "pistacheConfig.cmake"), "pistacheConfig.cmake")
        copy(join_path(os.path.dirname(__file__),
             "pistacheConfigVersion.cmake"), "pistacheConfigVersion.cmake")
        copy(join_path(os.path.dirname(__file__),
             "pistacheTargets.cmake"), "pistacheTargets.cmake")
        
    def install(self, spec, prefix):
        dest=prefix
        make()
        make('prefix=' + dest, 'install')
        install('pistacheConfig.cmake',prefix)
        install('pistacheConfigVersion.cmake',prefix)
        install('pistacheTargets.cmake',prefix)
