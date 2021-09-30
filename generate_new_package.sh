
name=$1
version=$2
origdir=$PWD

echo "Will attempt to create a package.py for the $version version of the $name package"

cd /tmp
url=https://codeload.github.com/DUNE-DAQ/$name/legacy.tar.gz/$version
curl -O $url
gtar ztvf $PWD/$version >/dev/null 2>&1

if [[ "$?" != "0" ]]; then
    echo "Either $url doesn't exist or it's not a tarball; returning..." >&2
    cd $origdir
    return 1
fi

cd $origdir
spack create --skip-editor $url

if [[ "$?" != 0 ]]; then
    echo "There was a problem trying to create a package off of ${url}, returning..." >&2
    cd $origdir
    return 3
fi

packagefile=dune-build/packages/$name/package.py

if ! [[ -e $packagefile ]]; then
    echo "The \"spack create $url\" command should have created $packagefile but didn't; returning..." >&2
    cd $origdir
    return 2
fi

if [[ ! -e ${packagefile}.backup ]]; then
    cp -p $packagefile{,.backup}
fi

# Get rid of the boilerplate between the "-"'s in the header comment
sed -i -r '/^# -/,/^# -/d' $packagefile

# Get rid of everything from the "depends_on-foo" example onwards
sed -i -r '/.*depends_on.*/,$d' $packagefile

# Set the homepage to the one on our official website (we assume it exists)
sed -i -r 's!homepage = ".*"!homepage = "https://dune-daq-sw.readthedocs.io/en/'$version'/packages/'$name'/"!' $packagefile

# Yours truly will maintain the Spack package
sed -i -r 's!^(\s*)#\s*maintainers.*!\1maintainers = ["jcfreeman2"]!' $packagefile

# Switch the auto-generated version from X.Y.Z to whatever was specified (e.g. dunedaq-vX.Y.Z)
sed -i -r 's/version\([^,]+,/version\("'$version'",/' $packagefile

# And since the new version probably means Spack can't auto-deduce the tarball, tell it explicitly what it is 
sed -i -r '/^\s*version/s!\)s*$!, extension="tar.gz", url="'$url'"\)!' $packagefile

echo "Please make your edits (e.g., add dependencies, remove FIXMEs, etc) by running \"spack edit $name\""

cat<<EF >> $packagefile

    def setup_run_environment(self, env):
        env.prepend_path('CET_PLUGIN_PATH', self.prefix.lib + "64")

EF

return 0
