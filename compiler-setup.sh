source  /home/spacknp/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/binutils-2.36.1-wozob7j2dmpqe2swmdnsltwiht2plxqe/binutils-setup.sh
BASE=/home/spacknp/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/gcc-8.2.0-tx65tffz7hcukcoyy35msh7e2rdnsmpk/ 

export PATH=$BASE/bin:$PATH
export MANPATH=$BASE/share/man:$MANPATH

if [ -e "${BASE}/lib64" ]; then
    export LD_LIBRARY_PATH="$BASE/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi
if [ -e "${BASE}/lib" ]; then
    # Add lib if exists
    export LD_LIBRARY_PATH="$BASE/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi



gcc_home=/home/spacknp/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/gcc-8.2.0-tx65tffz7hcukcoyy35msh7e2rdnsmpk/

export FC=`which gfortran`
export CC=`which gcc`
export CXX=`which g++`

export COMPILER_PATH=${gcc_home}
