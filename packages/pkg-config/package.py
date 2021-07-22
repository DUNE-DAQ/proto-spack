class PkgConfig(Package):

    homepage = "https://pkgconfig.freedesktop.org"

    url = "https://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz"

    version('0.29.2', sha256='6fc69c01688c9458a57eb9a1664c9aba372ccda420a02bf4429fe610e7e7d591')

    def install(self, spec, prefix):
        config_args = []
 
        config_args.append('--with-internal-glib')
        configure('--prefix={0}'.format(prefix), *config_args)

        make()
        make('install')
