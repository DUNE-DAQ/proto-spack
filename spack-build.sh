export HOME=/home/spacknp
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
cp binutils-setup.sh /home/spacknp/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/binutils-2.36.1-wozob7j2dmpqe2swmdnsltwiht2plxqe/

source compiler-setup.sh
which gcc
spack compilers
spack install -y folly@2021.05.24.00
spack install -y nlohmann-json@3.9.1
spack install -y pistache
spack install -y highfive@2.2.2
spack install -y cppzmq@4.3.0
spack install -y msgpack-c@3.3.0
spack install -y py-pybind11@2.6.2
spack install -y ipbus-software@2.8.0
spack install -y libzmq@4.3.4
spack install -y felix-software
