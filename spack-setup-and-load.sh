
echo "If you're not John Freeman hit Ctrl-c immediately!!"
sleep 5

required_host="epdtdi-spack-build03.cern.ch"
if [[ $(hostname) != $required_host ]]; then
    echo "Only run this on ${required_host}. Returning..." >&2
    return 1
fi

export HOME=/home/spacknp/jcfree
export EDITOR=/usr/bin/emacs

source spack/share/spack/setup-env.sh

cd ~/proto-spack
echo "JCF, Oct-4-2021: don't worry if you see \"Repository is already registered \" error message(s) below"
spack repo add dune-build 
spack repo add dune_daqpackages 
cd -

spack compiler find
spack load gcc@8.2.0
source proto-spack/compiler-setup.sh

spack load daq-cmake@issue161
spack load folly@2021.05.24.00
spack load nlohmann-json@3.9.1
spack load pistache
spack load highfive@2.2.2
spack load cppzmq@4.3.0
spack load msgpack-c@3.3.0
spack load py-pybind11@2.6.2
spack load ipbus-software@2.8.0
spack load libzmq@4.3.4
spack load felix-software
spack load hep-concurrency
spack load cetlib-except
spack load cetlib
spack load trace@v3_16_02
spack load py-moo
spack load ers@dunedaq-v2.8.0
spack load logging@dunedaq-v2.8.0
spack load cmdlib@dunedaq-v2.8.0
spack load opmonlib@dunedaq-v2.8.0
spack load rcif@dunedaq-v2.8.0
spack load appfwk@dunedaq-v2.8.0
spack load listrev@dunedaq-v2.8.0
