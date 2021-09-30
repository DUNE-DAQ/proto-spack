#!/bin/bash
if [ $# -ge 1 ]; then
  BUILD=$1; shift
else
  echo "$0: expecting 1 argument: [build type: release or debug] "
  return
fi


export HOME=$PWD
# cloning the spack repository 0.16
git clone https://github.com/spack/spack.git
# cloning the new dunedaq-spack repository
git clone https://github.com/DUNE-DAQ/proto-spack.git
# source the spack built-in configuration
source $HOME/spack/share/spack/setup-env.sh
# just test it
spack compilers 
# add the new dunedaq repo
cd proto-spack
spack repo add dune-build
cd $HOME
spack install gcc@8.2.0+binutils

spack load gcc@8.2.0
spack compiler find
spack compiler remove gcc@4.8.5
cp binutils-setup.sh $PWD/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/binutils-2.36.1-*/

source compiler-setup.sh
which gcc
spack compilers
if [[ "$BUILD" = "debug" ]]; then
spack -C $HOME/build-scopes/debug install -y trace build_type = Debug
spack -C $HOME/build-scopes/debug install -y cetpkgsupport build_type = Debug
spack -C $HOME/build-scopes/debug install -y folly@2021.05.24.00
spack -C $HOME/build-scopes/debug install -y nlohmann-json@3.9.1
spack -C $HOME/build-scopes/debug install -y pistache build_type = Debug 
spack -C $HOME/build-scopes/debug install -y highfive@2.2.2 build_type = Debug
spack -C $HOME/build-scopes/debug install -y msgpack-c@3.3.0 build_type = Debug
spack -C $HOME/build-scopes/debug install -y py-pybind11@2.6.2
spack -C $HOME/build-scopes/debug install -y ipbus-software@2.8.0
spack -C $HOME/build-scopes/debug install -y felix-software
spack -C $HOME/build-scopes/debug install -y cetmodules@2.25.05 build_type = Debug
spack -C $HOME/build-scopes/debug install -y hep-concurrency build_type = Debug
spack -C $HOME/build-scopes/debug install -y cetlib-except build_type = Debug
spack -C $HOME/build-scopes/debug install -y cetlib build_type = Debug

else if [[ "$BUILD" = "release" ]]; then

spack -C $HOME/build-scopes/release install -y trace
spack -C $HOME/build-scopes/release install -y cetpkgsupport 
spack -C $HOME/build-scopes/release install -y folly@2021.05.24.00
spack -C $HOME/build-scopes/release install -y nlohmann-json@3.9.1
spack -C $HOME/build-scopes/release install -y pistache 
spack -C $HOME/build-scopes/release install -y highfive@2.2.2 
spack -C $HOME/build-scopes/release install -y msgpack-c@3.3.0 
spack -C $HOME/build-scopes/release install -y py-pybind11@2.6.2
spack -C $HOME/build-scopes/release install -y ipbus-software@2.8.0
spack -C $HOME/build-scopes/release install -y felix-software
spack -C $HOME/build-scopes/release install -y cetmodules@2.25.05 
spack -C $HOME/build-scopes/release install -y hep-concurrency 
spack -C $HOME/build-scopes/release install -y cetlib-except 
spack -C $HOME/build-scopes/release install -y cetlib

fi

