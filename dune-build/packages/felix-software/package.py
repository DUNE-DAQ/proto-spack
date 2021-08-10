from spack import *
import os
import sys

from shutil import copytree
import spack.util.environment as envutil

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
#        install('*',prefix)
        copytree('.', prefix.software)

        with working_dir(prefix.software):

            bash = which('bash')

            my_path=os.environ['PATH']
            
            os.chdir(prefix.software)
            to_reverse = envutil.EnvironmentModifications()

            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/cmake_tdaq.git')
            os.system('sed -i \'2 i set(NOLCG TRUE)\' cmake_tdaq/cmake/modules/FELIX.cmake')
 
            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/drivers_rcc.git')
            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/flxcard.git')            

            os.system('sed -i \'s/REG_PCIE_ENDPOINTS/REG_PCIE_ENDPOINT/g\' flxcard/src/FlxCard.cpp')
            os.system('sed -i \'s/BF_PCIE_ENDPOINTS/BF_PCIE_ENDPOINT/g\' flxcard/src/flx-info.cpp')
            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/regmap.git')


            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/ftools.git')
            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/external-catch.git external/catch')
            os.system('git clone ssh://git@gitlab.cern.ch:7999/atlas-tdaq-felix/client-template.git')

            new_path = prefix+'/software/cmake_tdaq/bin:'
            os.environ['PATH'] = new_path + my_path



            os.system('cmake_config x86_64-centos7-gcc8-opt') 

            os.chdir("x86_64-centos7-gcc8-opt")

            make()
