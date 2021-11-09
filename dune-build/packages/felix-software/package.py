from spack import *
import os
import sys

from shutil import copytree
import spack.util.environment as envutil

class FelixSoftware(Package):

    #homepage = "https://gitlab.cern.ch/atlas-tdaq-felix/software"
    #git = "https://gitlab.cern.ch/atlas-tdaq-felix/software.git"
    git = "file:///home/spacknp/jcfree/software"

    #version('issue161', branch='johnfreeman/daq-buildtools_issue161')
    version('master', branch='master')


    depends_on('boost@1.75.0', type='build')
    depends_on('python@3.8.11', type='build')
    depends_on('cmake@3.20.5', type='build')
#    depends_on('qt@5.15.2', type='build')
    depends_on('intel-tbb@2020.3', type='build')
    depends_on('yaml-cpp@0.7.0', type='build')
    depends_on('czmq@4.1.1', type='build')
    depends_on('cppzmq@4.3.0', type='build')

    def patch(self):
        copy(join_path(os.path.dirname(__file__),
             "felixConfig.cmake"), self.prefix + "/felixConfig.cmake")
        copy(join_path(os.path.dirname(__file__),
             "felixConfigVersion.cmake"), self.prefix + "/felixConfigVersion.cmake")
        copy(join_path(os.path.dirname(__file__),
             "felixTargets.cmake"), self.prefix + "/felixTargets.cmake")

    def install(self, spec, prefix):

        copytree('.', prefix.software)

        with working_dir(prefix.software):

            bash = which('bash')

            my_path=os.environ['PATH']
            
            os.chdir(prefix.software)


            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/cmake_tdaq.git')
            os.system('sed -i \'2 i set(NOLCG TRUE)\' cmake_tdaq/cmake/modules/FELIX.cmake')
            os.system('pushd cmake_tdaq && git checkout 3f176ac && popd')
 
            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/drivers_rcc.git')
            os.system('pushd drivers_rcc && git checkout a3a453e && popd')
            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/flxcard.git')
            os.system('pushd flxcard && git checkout 8208c3a && popd')

            os.system('sed -i \'s/REG_PCIE_ENDPOINTS/REG_PCIE_ENDPOINT/g\' flxcard/src/FlxCard.cpp')
            os.system('sed -i \'s/BF_PCIE_ENDPOINTS/BF_PCIE_ENDPOINT/g\' flxcard/src/flx-info.cpp')
            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/regmap.git')
            os.system('pushd regmap && git checkout adc0025 && popd')

            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/packetformat.git')
            os.system('pushd packetformat && git checkout 15c0fc1 && popd')

            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/ftools.git')
            os.system('pushd ftools && git checkout 0dc8aca && popd')
            ftools_dir=prefix+"/software/ftools/"
            install('CMakeLists.txt',ftools_dir)
            os.system('git clone https://gitlab.cern.ch/atlas-tdaq-felix/external-catch.git external/catch')
            os.system('pushd external/catch && git checkout 6a9aa08 && popd')
            os.system('git clone ssh://git@gitlab.cern.ch:7999/atlas-tdaq-felix/client-template.git')
            os.system('pushd client-template && git checkout 390ec87 && popd')

            new_path = prefix+'/software/cmake_tdaq/bin:'
            os.environ['PATH'] = new_path + my_path
            os.system('cmake_config x86_64-centos7-gcc8-opt') 
            os.chdir("x86_64-centos7-gcc8-opt")
            make()

        # JCF, Oct-21-2021
        # Perform the same copies as in daq-release's build_felix.sh excepting ftools which may have build issues

        with working_dir(prefix):
        
            for subdir in ["include", "lib", "bin"]:
                os.mkdir(subdir)

            copytree("software/drivers_rcc", "drivers_rcc")
            copytree("software/regmap/regmap", "include/regmap")
            copytree("software/drivers_rcc/cmem_rcc", "include/cmem_rcc")
            copytree("software/drivers_rcc/rcc_error", "include/rcc_error")
            copytree("software/flxcard/flxcard", "include/flxcard")
            copytree("software/packetformat/packetformat", "include/packetformat")

            os.system("cp -p software/drivers_rcc/lib64/lib* lib")
            os.system("cp -r software/regmap/regmap include")
            os.system("cp -r software/drivers_rcc/cmem_rcc  include")
            os.system("cp -r software/drivers_rcc/rcc_error include")
            os.system("cp -r software/flxcard/flxcard include")
            os.system("cp -r software/packetformat/packetformat include")

            os.system("cp software/drivers_rcc/lib64/lib* lib")
            os.system("cp software/x86_64-centos7-gcc8-opt/flxcard/lib* lib")
            os.system("cp software/x86_64-centos7-gcc8-opt/packetformat/lib* lib")
            os.system("cp software/x86_64-centos7-gcc8-opt/regmap/lib* lib")
            os.system("cp software/x86_64-centos7-gcc8-opt/drivers_rcc/lib* lib")
            os.system("cp software/x86_64-centos7-gcc8-opt/flxcard/flx-* bin")

            os.system("rm -rf software")
