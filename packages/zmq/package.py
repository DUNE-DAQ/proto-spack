from spack import *


class Zmq(CMakePackage):

    homepage = "https://github.com/zeromq"
    url      = "https://github.com/zeromq/libzmq/archive/refs/tags/v4.3.4.tar.gz"

    version('4.3.4', sha256='0ff5a531c9ffaf0dfdc7dc78d13d1383088f454896d252934c429b2554d10559')

#    depends_on('autoconf@2.70', type='build')
#    depends_on('automake', type='build')
#    depends_on('libtool',  type='build')
#    depends_on('m4',       type='build')
    def cmake_args(self):
        options = []

        return options
