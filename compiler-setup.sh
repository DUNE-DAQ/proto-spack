#!/bin/bash                                                                                                                                               
if [ $# -ge 3 ]; then
    COMPILER=$1; shift
    VERSION=$1; shift
    ARCH=$1; shift
else
  echo "$0: expecting 3 arguments: [compiler: gcc] [compiler version: (e.g., 4.8.1) or native] [arch: centos7 or centos8]"
  return
fi

if [[ "$VERSION" != "native" ]]; then

    source $PWD/spack/opt/spack/linux-$ARCH-*/$COMPILER-$VERSION/binutils-*/binutils-setup.sh
    BASE=$HOME/spack/opt/spack/linux-$ARCH-*/$COMPILER-4.*/$COMPILER-$VERSION-*/ 

    export PATH=$BASE/bin:$PATH
    export MANPATH=$BASE/share/man:$MANPATH

    if [ -e "${BASE}/lib64" ]; then
	export LD_LIBRARY_PATH="$BASE/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
    fi
    if [ -e "${BASE}/lib" ]; then
	export LD_LIBRARY_PATH="$BASE/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
    fi

    gcc_home=$HOME/spack/opt/spack/linux-$ARCH-*/$COMPILER-4.*/$COMPILER-$VERSION-*/

else
    gcc_home=`which gcc`
fi


export FC=`which gfortran`
export CC=`which gcc`
export CXX=`which g++`

export COMPILER_PATH=${gcc_home}
