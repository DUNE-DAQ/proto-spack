source  $HOME/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/binutils-2.37-rlnsydsnert6nt4icx6jytx6kqfiel75/binutils-setup.sh
BASE=$HOME/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/gcc-8.2.0-gruolqa3jc23wu7a5zh6a4kylcbmcj76/

export PATH=$BASE/bin:$PATH
export MANPATH=$BASE/share/man:$MANPATH

if [ -e "${BASE}/lib64" ]; then
    export LD_LIBRARY_PATH="$BASE/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi
if [ -e "${BASE}/lib" ]; then
    # Add lib if exists
    export LD_LIBRARY_PATH="$BASE/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi



gcc_home=$BASE

export FC=`which gfortran`
export CC=`which gcc`
export CXX=`which g++`

export COMPILER_PATH=${gcc_home}
