# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class DuneDaqpackages(BundlePackage):
    """A dummy package meant to pull in all the packages in the DUNE DAQ suite"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/latest/"

    version("dunedaq-v2.8.0")

    # In general placing higher-level dependencies first to prevent clashes
    depends_on('minidaqapp@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('dfmodules@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('dqm@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('flxlibs@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('readout@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('trigger@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('timinglibs@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('triggeralgs@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('timing@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('dfmessages@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('nwqueueadapters@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('ipm@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('serialization@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('dataformats@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('appfwk@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('rcif@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('cmdlib@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('opmonlib@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('logging@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('ers@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')
    depends_on('daq-cmake@issue161', when='@dunedaq-v2.8.0')
    depends_on('trace@v3_16_02', when='@dunedaq-v2.8.0')
    depends_on('py-moo')
    depends_on('py-pexpect') # Needed for traditional workareas

    depends_on('listrev@dunedaq-v2.8.0', when='@dunedaq-v2.8.0')

