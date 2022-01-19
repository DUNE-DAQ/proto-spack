from spack import *
import os
import sys

from shutil import copytree
import spack.util.environment as envutil

class FelixSoftware(Package):

    git = "https://github.com/jcfreeman2/intentionallyempty.git"

    version("dunedaq-v2.8.0")


    depends_on('boost', type='build')
    depends_on('python', type='build')
    depends_on('cmake', type='build')
#    depends_on('qt@5.15.2', type='build')
#    depends_on('intel-tbb', type='build')
    depends_on('yaml-cpp@0.6.3', type='build')
    depends_on('czmq@4.1.1', type='build')
    depends_on('cppzmq', type='build')
    depends_on('py-pybind11', type=('build', 'link', 'run'))
    depends_on("nlohmann-json")

    def setup_build_environment(self, env):
        if not "REGMAP_VERSION" in os.environ:
            env.set("REGMAP_VERSION", "0x0500")

    def patch(self):
        copy(join_path(os.path.dirname(__file__),
             "felixConfig.cmake"), self.prefix + "/felixConfig.cmake")
        copy(join_path(os.path.dirname(__file__),
             "felixConfigVersion.cmake"), self.prefix + "/felixConfigVersion.cmake")
        copy(join_path(os.path.dirname(__file__),
             "felixTargets.cmake"), self.prefix + "/felixTargets.cmake")
        copy(join_path(os.path.dirname(__file__), 
            "CMakeLists_base_of_software_repo.txt"), "CMakeLists.txt")
        copy(join_path(os.path.dirname(__file__), 
                       "ftools_CMakeLists.txt"), "ftools_CMakeLists.txt")
        copy(join_path(os.path.dirname(__file__), 
                       "flxcard_py_CMakeLists.txt"), "flxcard_py_CMakeLists.txt")


    def install(self, spec, prefix):

        copytree('.', prefix.software)

        def return_zero_or_exit(cmd):
            retval = os.system(cmd)
            if retval != 0:
                sys.stderr.write(f"Error: return value of {retval} for the command \"{cmd}\"")
                sys.exit(retval)

        with working_dir(prefix.software):

            os.chdir(prefix.software)

            print("About to clone https://gitlab.cern.ch/atlas-tdaq-felix/cmake_tdaq.git")
            return_zero_or_exit('git clone https://gitlab.cern.ch/atlas-tdaq-felix/cmake_tdaq.git')
            return_zero_or_exit('sed -i \'2 i set(NOLCG TRUE)\' cmake_tdaq/cmake/modules/FELIX.cmake')
            return_zero_or_exit('pushd cmake_tdaq && git checkout d66ce21b && popd')
 
            print("About to clone https://gitlab.cern.ch/atlas-tdaq-felix/drivers_rcc.git")
            return_zero_or_exit('git clone https://gitlab.cern.ch/atlas-tdaq-felix/drivers_rcc.git')
            return_zero_or_exit('pushd drivers_rcc && git checkout b37bd757 && popd')
            print("About to clone https://gitlab.cern.ch/atlas-tdaq-felix/flxcard.git")
            return_zero_or_exit('git clone https://gitlab.cern.ch/atlas-tdaq-felix/flxcard.git')
            return_zero_or_exit('pushd flxcard && git checkout 683d9696 && popd')

            print("About to clone https://gitlab.cern.ch/atlas-tdaq-felix/regmap.git")
            return_zero_or_exit('git clone https://gitlab.cern.ch/atlas-tdaq-felix/regmap.git')
            return_zero_or_exit('pushd regmap && git checkout 87ce47ba && popd')

            print("About to clone https://gitlab.cern.ch/atlas-tdaq-felix/packetformat.git")
            return_zero_or_exit('git clone https://gitlab.cern.ch/atlas-tdaq-felix/packetformat.git')
            return_zero_or_exit('pushd packetformat && git checkout a84931eb && popd')

            print("About to clone https://gitlab.cern.ch/atlas-tdaq-felix/flxcard_py.git")
            return_zero_or_exit('git clone https://gitlab.cern.ch/atlas-tdaq-felix/flxcard_py.git')
            return_zero_or_exit('pushd flxcard_py && git checkout 61001bd6 && popd')
            install("flxcard_py_CMakeLists.txt", prefix+"/software/flxcard_py/CMakeLists.txt")

            print("Aout to clone https://gitlab.cern.ch/atlas-tdaq-felix/ftools.git")
            return_zero_or_exit('git clone https://gitlab.cern.ch/atlas-tdaq-felix/ftools.git')
            return_zero_or_exit('pushd ftools && git checkout 1cfd1b56 && popd')
            install('ftools_CMakeLists.txt', prefix+"/software/ftools/CMakeLists.txt")

            return_zero_or_exit('git clone https://gitlab.cern.ch/atlas-tdaq-felix/external-catch.git external/catch')
            return_zero_or_exit('pushd external/catch && git checkout 6a9aa08a && popd')

            os.environ['PATH'] = prefix+"/software/cmake_tdaq/bin" + ":" + os.environ['PATH']
            return_zero_or_exit('cmake_config x86_64-centos7-gcc8-opt') 
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

            return_zero_or_exit("cp software/drivers_rcc/lib64/lib* lib")
            return_zero_or_exit("cp software/x86_64-centos7-gcc8-opt/flxcard/lib* lib")
            return_zero_or_exit("cp software/x86_64-centos7-gcc8-opt/flxcard_py/lib* lib")
            return_zero_or_exit("cp software/x86_64-centos7-gcc8-opt/packetformat/lib* lib")
            return_zero_or_exit("cp software/x86_64-centos7-gcc8-opt/regmap/lib* lib")
            return_zero_or_exit("cp software/x86_64-centos7-gcc8-opt/drivers_rcc/lib* lib")
            return_zero_or_exit("cp software/x86_64-centos7-gcc8-opt/ftools/libFlxTools* lib")

            return_zero_or_exit("cp software/x86_64-centos7-gcc8-opt/flxcard/flx-* bin")
            return_zero_or_exit("cp software/x86_64-centos7-gcc8-opt/ftools/f* bin")

            return_zero_or_exit("rm -rf software")
