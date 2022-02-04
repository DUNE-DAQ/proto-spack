_JCF, Jan-19-2022: to try step-by-step instructions which exercise the latest-greatest in Spack support for DUNE DAQ packages, scroll down to the "Setting up the DUNE-DAQ packages and running the minidaqapp demo" section of this page_

_JCF, Jan-25-2022: be aware that as I work toward making the Spack development stack neater / more portable, sometimes the target packages meant to be loaded in by following the instructions (dune-daqpackages@dunedaq-v2.9.0, e.g.) will be uninstalled, in which case the instructions (temporarily) won't work. Please contact me if this is the case and I'll reinstall for you_

# proto-spack

# Testing: Machines
The following machines have been created to test the builds:
epdtdi-spack-build01, epdtdi-spack-build02 and epdtdi-spack-build03 reachable through the account: spacknp

## Setup of the build machine
The build machine has been set via puppet as a Centos7 base machine. The set of packages pre-installed in the system are the following (puppet repository: it-puppet-hostgroup-detector_interface. Specific spackdune.pp available at: code/manifest)

$pkgs_to_be_installed = [ 'python3.x86_64', 'python3-devel.x86_64', 'python3-libs.x86_64', 'java-1.8.0-openjdk.x86_64', 'java-1.8.0-openjdk-devel.x86_64', 'java-1.8.0-openjdk-headless.x86_64', 'gcc.x86_64', 'gcc-c++.x86_64', 'gcc-gfortran.x86_64', 'libgcc.x86_64', 
'bzip2.x86_64', 'bzip2-devel.x86_64', 'bzip2-libs.x86_64', 'unzip.x86_64', 'librdmacm.x86_64', 'libuuid-devel.x86_64' ]

$pkgs_pip_base = [ 'python34-setuptools_scm', 'python34-pip', 'python3-apipkg', 'python2-pip' ]

# Installing the DUNE DAQ suite in Spack form on a new machine

_JCF, Jan-31-2022: this is under construction_

The following instructions are applicable to a Centos7 node which has a default compiler `gcc4.8.5`. This works on CERN build machines. 
```
git clone -c feature.manyFiles=true https://github.com/spack/spack.git
cd spack
git checkout 7134cab8 # Probably the most recent tag, v0.17.1, would also work
cd ..
git clone -c feature.manyFiles=true https://github.com/DUNE-DAQ/proto-spack
. spack/share/spack/setup-env.sh
spack compiler find  # Should add the /usr/bin gcc compiler to ~/.spack/linux/compilers.yaml
cd proto-spack/
spack repo add dune-build
spack repo add dune_daqpackages
spack install systems@dunedaq-v2.9.0  # 60-90 minutes on epdtdi-spack-build02
```
You'll now have gcc 8.2.0 and python 3.8.3, both built with the system gcc. Now let's tell Spack that gcc 8.2.0 is available:
```
spack load systems@dunedaq-v2.9.0
spack compiler find # Should add the gcc 8.2.0 you just built to ~/.spack/linux/compilers.yaml 
```

Now we install dune-daqpackages:
```
spack install dune-daqpackages@dunedaq-v2.9.0 
```
...keeping in mind that some of the gitlab-located packages (e.g., cetlib) will require you to enter your username and password for access. 

# Development: Steps using any of the epdtdi-spack-build0X machines:

To read the official documentation on how to get started building with Spack, go [here](https://spack-tutorial.readthedocs.io/en/latest/tutorial_basics.html). However, since Spack has already been installed on epdtdi-spack-build03, you can just kick things off after you login with the following standard source:

source $HOME/spack/share/spack/setup-env.sh

and then you can run `spack find`, `spack install <pkg>`, etc.

## Setting up the DUNE-DAQ packages and running the minidaqapp demo 

As of the most recent non-documentation commit (d5ced499f4d169ed277c7, Dec-6-2021) it's possible to recreate the minidaqapp demo found in the ["Instructions for Casual Users" section of the minidaqapp documentation](https://dune-daq-sw.readthedocs.io/en/latest/packages/minidaqapp/InstructionsForCasualUsers/), except instead of using ups packages you'll be using Spack packages. To see this (and to learn a bit more about the work done getting DUNE-DAQ packages spackified), log in to epdtdi-spack-build03 and do the following to start working in my (JCF) area:
```
export HOME=/home/spacknp/jcfree
cd ~
. daq-buildtools/env.sh  # May want to check that you're on the johnfreeman/issue161_spack branch
dbt-create.sh --spack <frozen release> <name of workarea>  # dunedaq-v2.9.0 (when installed) currently supported
cd <name of workarea>
dbt-workarea-env --spack
```
...where `dbt-workarea-env --spack` will load in `dune-daqpackages`. Note that if you leave out the `--spack` argument either in `dbt-create.sh` or `dbt-workarea-env` that ups will be used instead of Spack. 

At this point, you can run the demo by starting at point (7) of the [instructions for the minidaqapp demo](https://dune-daq-sw.readthedocs.io/en/latest/packages/minidaqapp/InstructionsForCasualUsers/)

If you run `spack find` you'll see DUNE DAQ packages up through dune-daqpackages on the chain. We can also get `spack find` to be more informative. E.g., `spack find -N` will tell you which repo each package belongs to. `builtin` means it's outside our purview, `dune-build` corresponds to the DUNE external packages (folly, etc.) and `dune_daqpackages` corresponds to the DAQ packages (cmdlib, etc.). `spack repo list` will tell you which repos are available. `spack find -d dune-daqpackages@dunedaq-v2.9.0 build_type=RelWithDebInfo` will tell you how the dependencies for our dummy package work in spack. 

Note that as of Dec-9-2021, you can get `dbt-workarea-env` to work with Spack package sets if you're using the `johnfreeman/issue161_spack branch` branch of daq-buildtools; this is analogous to the standard ups behavior of `dbt-workarea-env` when you're using a versioned daq-buildtools. E.g., the following:
```
dbt-workarea-env --spack -s externals
```
...will load the external packages, but not the DUNE DAQ-specific packages, from the frozen release corresponding to your work area. 

Note that as of Jan-18-2022, you now have the option of running `dbt-setup-release` just as you do when ups is used instead of Spack. E.g. `dbt-setup-release --spack dunedaq-v2.9.0` will set up the dunedaq-v2.9.0 frozen release suite of packages. 


