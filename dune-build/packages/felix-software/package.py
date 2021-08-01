from spack import *
import os
import sys
from shutil import copytree

class FelixSoftware(Package):

    homepage = "https://gitlab.cern.ch/atlas-tdaq-felix/software"
    git = "https://gitlab.cern.ch/atlas-tdaq-felix/software.git"

    version('master', branch='master')


    depends_on('boost@1.75.0', type='build')
    depends_on('python@3.8.11', type='build')
    depends_on('cmake@3.20.5', type='build')
    depends_on('qt@5.15.2', type='build')
    depends_on('intel-tbb@2020.3', type='build')
    depends_on('yamlcpp@0.7.0', type='build')
    depends_on('zeromq@4.1.8', type='build')

    def install(self, spec, prefix):
        install('*',prefix)
        with working_dir(prefix):

            bash = which('bash')
            bash(join_path('clone_all.sh'), prefix)
            bash(join_path('setup.sh'), prefix)


#        os.chdir(prefix)
#        mkdir(prefix.toto)
#        copytree('software', prefix.software)
#        mkdir(prefix.toto)
        #        with working_dir(self.build_directory):
#        bash = which('bash')
#        bash('./clone_all.sh https')

#        configure('--prefix=%s' % prefix)
#        make()
#        make('install')
