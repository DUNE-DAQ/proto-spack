from spack import *


class NlohmannJson(CMakePackage):

    homepage = "https://github.com/nlohmann/json"
    url      = "https://github.com/nlohmann/json/archive/refs/tags/v3.9.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.9.1', sha256='4cf0df69731494668bdd6460ed8cb269b68de9c19ad8c27abc24cd72605b2d5b')

    # FIXME: Add dependencies if required.
#    depends_on('m4', type='build')
#    depends_on('autoconf@2.70', type='build')
#    depends_on('automake@1.16.3', type='build')
#    depends_on('libtool', type='build')

    def cmake_args(self):
        options = []

        return options
