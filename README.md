# proto-spack
Warning: None of the external packages (besides cmake) will work with a vanilla installation of the gcc8.2.0. It is mandatory that this compiler is built linkig it against a binutils installation first
NOTE: The packages provided by spack (builtin) are included in this repository in the so called builtin-spack-packages

# Building gcc@8.2.0
The following instructions are applicable to a Centos7 node which has a default compiler gcc4.8.5
## Ensure gcc will be built against binutils
Edit the packages.yaml file of gcc and enables to True the binutils flag
At this point no particular requirements are needed, you can launch the "spack install gcc@8.2.0" order. The binutils package will be installed as dependency.  
The new compiler can be chosen to build the rest of packages. ensure the compiler defined in default in the machine points to this new package. for this reason, reconfigure the compilers.yaml file of spack following this example:
