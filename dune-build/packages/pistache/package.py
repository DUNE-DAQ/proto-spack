# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import os
import sys

class Pistache(CMakePackage):
    """An elegant C++ REST framework."""

    homepage = "http://pistache.io"
    url      = "https://github.com/oktal/pistache/archive/v0.0.0.tar.gz"
    git      = "https://github.com/oktal/pistache.git"

    maintainers = ['jcfreeman2']

    # JCF, Oct-23-2021

    # Commit a54a4fab00252a9 dates from Oct-6-2020 on the master
    # branch of pistache, whereas the version in ups is dated
    # Oct-7-2020. Between that and the header files (at the very
    # least) being identical between the ups product and the commit hash's, 
    # it's probably a safe bet that this is the hash we want

    version('dunedaq-v2.8.0', commit="a54a4fab00252a9")
    version('master', branch='master')
    depends_on('openssl')
    depends_on('libpthread-stubs')

    def patch(self):
        os.mkdir(self.prefix + "/lib64")

        copy(join_path(os.path.dirname(__file__),
             "PistacheConfig.cmake"), self.prefix + "/PistacheConfig.cmake")
        copy(join_path(os.path.dirname(__file__),
             "PistacheConfigVersion.cmake"), self.prefix + "/PistacheConfigVersion.cmake")
        copy(join_path(os.path.dirname(__file__),
             "PistacheTargets.cmake"), self.prefix + "/PistacheTargets.cmake")
        copy(join_path(os.path.dirname(__file__),
             "PistacheTargets-release.cmake"), self.prefix + "/PistacheTargets-release.cmake")

        print(f"IN THE PATCH, cwd == {os.getcwd()}")
        os.system("find . -name \"*.so\"")
        print("Just looked for shared object libraries")
      
    def setup_build_environment(self, env):
        env.prepend_path("DUNEDAQ_SHARE_PATH", self.prefix + "/share")
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

    def install(self, spec, prefix):
        super().install(spec, prefix)

        print([f for f in dir(CMakePackage) if not f.startswith('_')])
        print(self.build_directory)
        os.system(f"cp -p {self.build_directory}/src/*.so* {self.prefix}/lib64")
        #print(f"cp -rp {self.stage.source_path}/include {self.prefix}/include")
        #os.system(f"cp -rp {self.stage.source_path}/include {self.prefix}/include")
        #print(f"source_path is {self.stage.source_path}")
