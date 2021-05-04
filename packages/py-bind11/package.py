from spack import *


class PyBind11(PythonPackage):

    homepage = "https://github.com/pybind/pybind11"
    pypi = "pybind11/pybind11-2.6.2.tar.gz"

    version('2.6.2', sha256='8ff2fff22df038f5cd02cea8af56622bc67f5b64534f1b83b9f133b8366acff2')

    depends_on('py-setuptools', type='build')


    def install(self, spec, prefix):
        setup_py('install', '--root=/', '--prefix={0}'.format(prefix))
