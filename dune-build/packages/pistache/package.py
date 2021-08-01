# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install pistache
#
# You can edit this file again by typing:
#
#     spack edit pistache
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Pistache(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/oktal/pistache"
    url      = "https://github.com/oktal/pistache/archive/v0.0.0.tar.gz"
    git      = "https://github.com/oktal/pistache.git"

    maintainers = ['brettviren']

    version('master', branch='master')
    depends_on('openssl')
    depends_on('libpthread-stubs')
