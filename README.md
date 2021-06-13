# proto-spack
Warning: None of the external packages (besides cmake) will work with a vanilla installation of the gcc8.2.0. It is mandatory that this compiler is built linkig it against a binutils installation first
NOTE: The packages provided by spack (builtin) are included in this repository in the so called builtin-spack-packages

## Building `gcc@8.2.0`
The following instructions are applicable to a Centos7 node which has a default compiler `gcc4.8.5`
### Ensure gcc will be built against binutils
Edit the `packages.yaml` file of gcc and enables to True the binutils flag
At this point no particular requirements are needed, you can launch the `spack install gcc@8.2.0` order. The binutils package will be installed as dependency.  
The new compiler can be chosen to build the rest of packages. ensure the compiler defined in default in the machine points to this new package. for this reason, reconfigure the `compilers.yaml` file of spack just pointing to the proper positions of the executables: `gcc`, `gfortran` and `g++` which have to be included into the env variables:
```
cc
cxx
f77
fc
```
Which are already predefined into the mentioned file
In addition, be sure the compiler used in the machine is compatible with the version used in spack. for that aim, you can created a setup compiler file which could look like:

```sh
source  /home/pmendez/workspace/DUNE-Spack/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/binutils-2.35.1-trlunea2wrla66inkwnhomsrr4vntund/setup.sh
BASE=/home/pmendez/workspace/DUNE-Spack/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/gcc-8.2.0-zfho7gkmt5payd36q7nwlk6n6xv4eum3/

export PATH=$BASE/bin:$PATH
export MANPATH=$BASE/share/man:$MANPATH

if [ -e "${BASE}/lib64" ]; then
    export LD_LIBRARY_PATH="$BASE/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi
if [ -e "${BASE}/lib" ]; then
    # Add lib if exists
    export LD_LIBRARY_PATH="$BASE/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi



gcc_home=/home/pmendez/workspace/DUNE-Spack/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/gcc-8.2.0-zfho7gkmt5payd36q7nwlk6n6xv4eum3/

export FC=`which gfortran`
export CC=`which gcc`
export CXX=`which g++`

export COMPILER_PATH=${gcc_home}
```

where the binutils setup file is:

```sh
BASE=/home/pmendez/workspace/DUNE-Spack/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/binutils-2.35.1-trlunea2wrla66inkwnhomsrr4vntund/

export PATH=$BASE/bin:$PATH
export MANPATH=$BASE/share/man:$MANPATH

if [ -e "${BASE}/lib64" ]; then
    export LD_LIBRARY_PATH="$BASE/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi

if [ -e "${BASE}/lib" ]; then
    
    export LD_LIBRARY_PATH="$BASE/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi
```
