from spack import *
class Zeromq(AutotoolsPackage):

    homepage = "https://zeromq.org/"

    url = "https://github.com/zeromq/zeromq4-1/archive/refs/tags/v4.1.8.tar.gz"

    version('4.1.8', sha256='d1b8fb7a79a0d435eff2bace33c40f56b2400980e4380586aea032d26a53f311')

    depends_on('libsodium@1.0.18', type='build')
    depends_on('pkg-config@0.29.2', type='build')
    depends_on('libtool',    type='build')
#    depends_on('autoconf',    type='build')
#    depends_on('automake',    type='build')



    def autoreconf(self, spec, prefix):
        Executable('./autogen.sh')()


    def install(self, spec, prefix):
        config_args = []
        config_args.append('--with-libsodium=yes')
        configure('--prefix={0}'.format(prefix), *config_args)

        make()
        make('install')
