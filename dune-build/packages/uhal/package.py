from spack import *
from spack.util.environment import is_system_path
import sys
import os

class Uhal(Package):

    homepage = "https://github.com/ipbus/"
    url      = "https://github.com/ipbus/ipbus-software/archive/refs/tags/v2.8.0.tar.gz"


    version('2.8.0', sha256='c452d4763fd8badd00cb7aa39174b4c53a2b5ac645245e553deaad882dff3c10')

    #depends_on('boost@1.75.0+debug', type='build')
    depends_on('boost@1.75.0', type='build')
    depends_on('pugixml@1.11.4', type='build')
    depends_on('gettext@0.21', type=('build', 'link', 'run'))
    depends_on('py-pybind11@2.6.2', type=('build', 'link', 'run'))

    patch('ipbus_2.patch', when='@2.8.0')

    def setup_build_environment(self,env):
        spec=self.spec
        env.set('Set','uhal')
        

        def add_include_path(dep_name):
            include_path = spec[dep_name].prefix.include
            if not is_system_path(include_path):
                env.append_path('SPACK_INCLUDE_DIRS', include_path)

        # With that done, let's go fixing those deps                                                                                                                                                                                                                    
        add_include_path('boost')
        add_include_path('pugixml')

        env.set('EXTERN_BOOST_INCLUDE_PREFIX', spec['boost'].prefix.include.boost)
        env.set('EXTERN_BOOST_LIB_PREFIX', spec['boost'].prefix.lib)
        env.set('EXTERN_PUGIXML_INCLUDE_PREFIX', spec['pugixml'].prefix.include)
        env.set('EXTERN_PUGIXML_LIB_PREFIX', spec['pugixml'].prefix.lib64)

    def patch(self):
        copy(join_path(os.path.dirname(__file__),
             "uhalConfig.cmake"), "uhalConfig.cmake")
        copy(join_path(os.path.dirname(__file__),
             "uhalConfigVersion.cmake"), "uhalConfigVersion.cmake")
        copy(join_path(os.path.dirname(__file__),
             "uhalTargets.cmake"), "uhalTargets.cmake")
        
    def install(self, spec, prefix):
        dest=prefix
        make()
#        make('install')
        make('prefix=' + dest, 'install')
        install('uhalConfig.cmake',prefix)
        install('uhalConfigVersion.cmake',prefix)
        install('uhalTargets.cmake',prefix)

