# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class DuneDaqpackages(BundlePackage):
    """A dummy package meant to pull in all the packages in the DUNE DAQ suite"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/latest/"

    version("dunedaq-v2.8.0")

    depends_on('minidaqapp@4.0.0', when='@dunedaq-v2.8.0')
    depends_on('dfmodules@2.2.1', when='@dunedaq-v2.8.0')
    depends_on('dqm@1.0.0', when='@dunedaq-v2.8.0')
    depends_on('flxlibs@1.2.1', when='@dunedaq-v2.8.0')
    depends_on('readout@1.4.2', when='@dunedaq-v2.8.0')
    depends_on('trigger@1.1.2', when='@dunedaq-v2.8.0')
    depends_on('timinglibs@1.2.0', when='@dunedaq-v2.8.0')
    depends_on('triggeralgs@0.3.0', when='@dunedaq-v2.8.0')
    depends_on('timing@5.5.1', when='@dunedaq-v2.8.0')
    depends_on('dfmessages@2.2.0', when='@dunedaq-v2.8.0')
    depends_on('nwqueueadapters@1.4.0', when='@dunedaq-v2.8.0')
    depends_on('ipm@2.2.0', when='@dunedaq-v2.8.0')
    depends_on('serialization@1.2.2', when='@dunedaq-v2.8.0')
    depends_on('dataformats@3.0.0', when='@dunedaq-v2.8.0')
    depends_on('appfwk@2.3.2', when='@dunedaq-v2.8.0')
    depends_on('rcif@1.1.1', when='@dunedaq-v2.8.0')
    depends_on('cmdlib@1.1.4', when='@dunedaq-v2.8.0')
    depends_on('opmonlib@1.3.2', when='@dunedaq-v2.8.0')
    depends_on('logging@1.0.3', when='@dunedaq-v2.8.0')
    depends_on('ers@1.1.3', when='@dunedaq-v2.8.0')
    depends_on('daq-cmake@issue161', when='@dunedaq-v2.8.0')
    depends_on('trace@v3_16_02', when='@dunedaq-v2.8.0')

    depends_on('listrev@2.1.4', when='@dunedaq-v2.8.0')
    depends_on('restcmd@1.1.3', when='@dunedaq-v2.8.0')
    depends_on('erskafka@1.3.0', when='@dunedaq-v2.8.0')
    depends_on('trigemu@2.3.0', when='@dunedaq-v2.8.0')
    depends_on('erses@1.0.0', when='@dunedaq-v2.8.0')
    depends_on('influxopmon@1.4.0', when='@dunedaq-v2.8.0')

