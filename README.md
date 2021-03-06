# proto-spack
Warning: None of the external packages (besides cmake) will work with a vanilla installation of the gcc8.2.0. It is mandatory that this compiler is built linking it against a binutils installation first
NOTE: The packages provided by spack (builtin) are included in this repository in the so called builtin-spack-packages

## Setup of the build machine
The build machine has been set via puppet as a Centos7 base machine. The set of packages pre-installed in the system are the following (puppet repository: it-puppet-hostgroup-detector_interface. Specific spackdune.pp available at: code/manifest)

$pkgs_to_be_installed = [ 'python3.x86_64', 'python3-devel.x86_64', 'python3-libs.x86_64', 'java-1.8.0-openjdk.x86_64', 'java-1.8.0-openjdk-devel.x86_64', 'java-1.8.0-openjdk-headless.x86_64', 'gcc.x86_64', 'gcc-c++.x86_64', 'gcc-gfortran.x86_64', 'libgcc.x86_64', 
'bzip2.x86_64', 'bzip2-devel.x86_64', 'bzip2-libs.x86_64', 'unzip.x86_64', 'librdmacm.x86_64', 'libuuid-devel.x86_64' ]

$pkgs_pip_base = [ 'python34-setuptools_scm', 'python34-pip', 'python3-apipkg', 'python2-pip' ]


## Building `gcc@8.2.0`
The following instructions are applicable to a Centos7 node which has a default compiler `gcc4.8.5`
### Ensure gcc will be built against binutils
spack install gcc@8.2.8+binutils 

is enogh to ensure the installation of the gcc8.2.0 compiler using binutils.   
The new compiler can be chosen to build the rest of packages. Ensure the compiler defined in default in the machine points to this new package. For this reason, reconfigure the `compilers.yaml` file of spack just pointing to the proper positions of the executables: `gcc`, `gfortran` and `g++` which have to be included into the env variables:
```
cc
cxx
f77
fc
```
Which are already predefined into the mentioned file

Once the gcc8.2.0 compiler has been built, the compilers.yaml file of the local spack configuration should be modified to point to the new distribution 

# Testing: Machines
The following machines have been created to test the builds:

epdtdi-spack-build01, epdtdi-spack-build02 and epdtdi-spack-build03 reachable through the account: spacknp

# Testing: Steps using epdtdi-spack-build02:

Download the spack v0.16 software: git clone https://github.com/spack/spack.git

cd /home/spacknp

source spack-setup.sh (Set the spack configuration and the HOME directory)

source setup_compuler.sh (Set the local compiler to the gcc8.2.0 already compiled using binutils through the local spack implementation)

# List of external DUNE packages

cetlib 3.11.01 -- Provided by SCISOFT

trace 3.16.02 -- Provided by SCISOFT

folly 2021.05.24.00 -- SPACK builtin 

nlohmann_json 3.9.1 -- SPACK builtin

pistache 2020.10.07 (master) -- Provided by the proto-spack repository

highfive 2.2.2 -- SPACK builtin

libzmq 4.3.4 -- SPACK builtin

cppzmq 4.3.0 -- SPACK builtin

msgpack-c 3.3.0 -- SPACK builtin

Felix (master) -- Provided by proto-spack repository together with all dependencies

py-pybind11 2.6.2 -- SPACK bultin

uhal 2.8.0 -- Provided by proto-spack repository with all dependencies

## Built example

The dunedaq-spack repository is already added to the local spack configuration in both build machines. Therefore, once you have log in, you just need to build any of the mentioned packages executing the command:

spack install <package_name>@<version_number>

for example: spack py-pybind11@2.6.2




`
