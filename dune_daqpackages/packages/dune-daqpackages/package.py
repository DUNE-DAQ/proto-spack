# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class DuneDaqpackages(BundlePackage):
    """A dummy package meant to pull in all the packages in the DUNE DAQ suite"""

    homepage = "https://dune-daq-sw.readthedocs.io/en/latest/"

    version("dunedaq-v2.8.0")
    version("dunedaq-v2.8.2")

    variant('build_type', default='RelWithDebInfo',
            description='The build type to build',
            values=('Debug', 'Release', 'RelWithDebInfo'),
            multi=True)

    for build_type in ["Debug", "RelWithDebInfo", "Release"]:

        depends_on(f'minidaqapp@4.0.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'dfmodules@2.2.1 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'dqm@1.0.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'flxlibs@1.2.1 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'readout@1.4.2 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'trigger@1.1.2 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'timinglibs@1.2.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'triggeralgs@0.3.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'timing@5.5.1 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'dfmessages@2.2.0 build_type={build_type}', when='@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'nwqueueadapters@1.4.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'ipm@2.2.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'serialization@1.2.2 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'dataformats@3.0.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'appfwk@2.3.2 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'rcif@1.1.1 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'cmdlib@1.1.4 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'opmonlib@1.3.2 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'logging@1.0.3 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'ers@1.1.3 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'daq-cmake@issue161 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'trace@v3_16_02 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'listrev@2.1.4 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'restcmd@1.1.3 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'erskafka@1.3.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'trigemu@2.3.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'erses@1.0.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'influxopmon@1.4.0 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')
        depends_on(f'lbrulibs@1.0.3 build_type={build_type}', when=f'@dunedaq-v2.8.0 build_type={build_type}')

        depends_on(f'minidaqapp@4.1.3 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'dqm@1.1.6 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'flxlibs@1.2.3 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'readout@1.4.5 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'trigger@1.1.3 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'triggeralgs@0.3.1 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'timing@5.7.0 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'timinglibs@1.4.0 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'dfmodules@2.3.2 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'daqdataformats@3.2.1 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'detdataformats@3.2.1 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'detchannelmaps@1.0.2 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'dfmessages@2.2.1 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'listrev@2.1.4 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'ipm@2.2.0 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'serialization@1.2.2 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'appfwk@2.3.3 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'rcif@1.1.1 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'cmdlib@1.1.4 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'opmonlib@1.3.4 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'logging@1.0.3 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'ers@1.1.3 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'daq-cmake@issue161 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'trace@v3_16_02 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'listrev@2.1.4 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'restcmd@1.1.3 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'erskafka@1.3.0 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'trigemu@2.3.1 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'erses@1.0.0 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'influxopmon@1.5.2 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
        depends_on(f'lbrulibs@1.0.5 build_type={build_type}', when=f'@dunedaq-v2.8.2 build_type={build_type}')
