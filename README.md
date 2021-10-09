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

## Setting up the DUNE-DAQ packages

As of the most recent non-documentation commit (e3376157c989c, Oct-8-2021) it's possible to recreate the listrev demo found in the ["Running" section of the daq-buildtools documentation](https://dune-daq-sw.readthedocs.io/en/latest/packages/daq-buildtools/#running), except instead of using ups packages you'll be using spack packages. To see this (and to learn a bit more about the work done getting DUNE-DAQ packages spackified), log in to epdtdi-spack-build03 and do the following to start working in my (JCF) area:
```
export HOME=/home/spacknp/jcfree
cd ~
source spack/share/spack/setup-env.sh
```
Now set up an environment for yourself. Let's pretend you call it `MyArea`:
```
spack env list   # Optional, tells you if there's an existing environment which already uses your name
spack env create MyArea
spack env activate MyArea
```
In your environment, no packages are yet loaded (`spack find`). They (probably) _are_ installed, but the environment is ignoring them. However, you can still get info on them. E.g., 
```
spack info dune-daqpackages
```
...where `dune-daqpackages` is a "dummy" package whose job it is to pull in other packages (see [here](https://spack.readthedocs.io/en/latest/workflows.html#dummy-packages) for more on this approach). You can also directly look at the `package.py` file which defines `dune-daqpackages`:
```
spack edit dune-daqpackages
```
...though don't edit it without consulting me first. 

Now let's load the package:
```
spack load dune-daqpackages@dunedaq-v2.8.0
```
It's possible that if I've been playing around with the packages that it's currently uninstalled, in which case you'll get a message like
```
==> Error: Spec 'dune-daqpackages@dunedaq-v2.8.0' matches no installed packages.
```
in this case, first install it, and then perform the load:
```
spack install dune-daqpackages@dunedaq-v2.8.0
spack load dune-daqpackages@dunedaq-v2.8.0
```
Now if you run `spack find` you'll see DUNE DAQ packages up through listrev on the chain. We can also get `spack find` to be more informative. E.g., `spack find -N` will tell you which repo each package belongs to. `builtin` means it's outside our purview, `dune-build` corresponds to the DUNE external packages (folly, etc.) and `dune_daqpackages` corresponds to the DAQ packages (cmdlib, etc.). `spack repo list` will tell you which repos are available. `spack find -d dune-daqpackages@dunedaq-v2.8.0` will tell you how the dependencies for our dummy package work in spack. 

I should add that there are currently (Oct-9-2021) a couple of differences between the `package.py`'s I have for the externals vs. what Patricia did. E.g., for folly (`spack edit folly`) you'll see that I build folly as a shared library and also have a patch which Phil created last year which prevents a linking error related to gflags. Also note I've created a `trace@v3_16_02`; this is the same TRACE version as used in the dunedaq-v2.8.0 release but with a patch which removes the dependency on cetmodules - a dependency that ruins the `TRACEConfig.cmake` file which gets produced when TRACE is built.

If you want to run listrev, you can now just do the following:
```
daq_application -n pippo -c stdin://$HOME/Documents/list-reversal-app.json
```
If you want to perform development, you can just set up a work area like so:
```
cd ~
. daq-buildtools/env.sh
dbt-create.sh dunedaq-v2.8.0 <name of work area>
cd <name of work area>
dbt-workarea-env-spack
```
and then develop normally. E.g., you can build `dataformats`. This won't, of course, currently (Oct-9-2021) work for all packages because some of the externals are lacking CMake config files. 
