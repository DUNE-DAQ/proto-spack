#!/bin/bash
if [ $# -ge 1 ]; then
  environment=$1; shift
else
  echo "$0: expecting 1 argument: [name of the environment] "
  return
fi

source $HOME/spack/share/spack/setup-env.sh

spack env create $environment
spack env activate $environment


echo "starting with the compiler gcc"
spack add gcc@8.2.0
echo "adding cmake"
spack add cmake@3.20.5
echo "adding folly"
spack add folly@2021.05.24.00
echo "adding trace"
spack add trace
echo "adding cetpkgsupport"
spack add cetpkgsupport
echo "adding nlohmann-json"
spack add nlohmann-json@3.9.1
echo "adding pistache"
spack add pistache
echo "adding highfive"
spack add highfive@2.2.2
echo "adding msgpack-c"
spack add msgpack-c@3.3.0
echo "adding pybind11"
spack add  py-pybind11@2.6.2
echo "adding ipbus-sfotware"
spack add ipbus-software@2.8.0
echo "adding libzmq"
spack add libzmq@4.3.4
echo "adding felix-software"
spack add felix-software
echo "adding cetmodules"
spack add cetmodules@2.25.05
echo "adding hep-concurrency"
spack add hep-concurrency
echo "adding cetlib-except"
spack add cetlib-except
echo "adding cetlib"
##spack add cetlib

spack concretize
