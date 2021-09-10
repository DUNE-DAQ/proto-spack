
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

spack compiler find
spack load gcc@8.2.0
source proto-spack/compiler-setup.sh

spack load daq-cmake
spack load folly@2021.05.24.00
spack load nlohmann-json@3.9.1
spack load pistache
spack load highfive@2.2.2
spack load cppzmq@4.3.0
spack load msgpack-c@3.3.0
spack load /lrrb52w  # py-pybind11@2.6.2
spack load ipbus-software@2.8.0
spack load libzmq@4.3.4
spack load felix-software
echo "Skipping load of cetmodules, it ruins the creation of TRACEConfig.cmake"
#spack load cetmodules@2.25.05
spack load hep-concurrency
spack load cetlib-except
spack load cetlib
spack load ers
spack load trace@v3_16_02

