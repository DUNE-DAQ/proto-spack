from spack import *


class Libsodium(Package):


    homepage = "https://libsodium.org"
    url      = "https://download.libsodium.org/libsodium/releases/libsodium-1.0.18.tar.gz"

    version('1.0.18', sha256='6f504490b342a4f8a4c4a02fc9b866cbef8622d5df4e5452b46be121e46636c1')


    def install(self, spec, prefix):
        configure('--prefix=%s' % prefix)
        make()
        make('install')

