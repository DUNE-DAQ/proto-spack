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

# Testing: Steps using any of the epdtdi-spack-build0X machines:

Download the script: https://github.com/DUNE-DAQ/proto-spack/blob/98318b8e6f38a2717d8aaee9817f20356f828603/spack-build.sh

and execute it. This script is intended to install locally all externals and dependencies. It will also install the gcc8.2.0 compiler already interfaced with binutils.

# List of external DUNE packages

cetlib 3.11.01 -- Provided by the proto-spack repository

cetmodules 2.25.05 -- Provided by the proto-spack repository

trace (master) -- Provided by the proto-spack repository

cetlib-except 1.07.04 -- Provided by the proto-spack repository

hep-concurrency 1.07.04 -- Provided by the proto-spack repository

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

## John's work notes

Doing the following, you can set up a work area and build cmdlib using Spack and not ups. Upon logging in to epdtdi-spack-build03:
```
. home/spacknp/jcfree/source_me
cd ~
```
Probably on top of the externals, the dunedaq-v2.8.0 versions of ers
and logging will also be installed. If not, then you can install them
using their `package.py`'s which have been added to
`dune-build/packages`. Also note I've created a `trace@v3_16_02`; this
is the same TRACE version as used in the dunedaq-v2.8.0 release but
with a patch which removes the dependency on cetmodules - a dependency
that ruins the `TRACEConfig.cmake` file which gets produced when TRACE
is built.

Assuming trace@v3_16_02, ers@dunedaq-v2.8.0 and logging@dunedaq-v2.8.0
are installed, you can load all the Spack packages you need via:
```
. proto-spack/spack-setup-and-load.sh
```
...which is essentially a modified fork of `/home/spacknp/spack-build.sh`. 

Now set up the daq-buildtools environment using
`daq-buildtools/env.sh` and `dbt-create.sh`. When you `cd` into the
new workarea, run `dbt-workarea-env-spack`. You'll now be able to
clone the dunedaq-v2.8.0 tag of cmdlib and build it...entirely against
Spack packages, _not_ ups packages.
