
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

spack load dune-daqpackages@dunedaq-v2.8.0
