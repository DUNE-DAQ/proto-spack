BASE=/home/spacknp/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/binutils-2.36.1-wozob7j2dmpqe2swmdnsltwiht2plxqe/

export PATH=$BASE/bin:$PATH
export MANPATH=$BASE/share/man:$MANPATH

if [ -e "${BASE}/lib64" ]; then
    export LD_LIBRARY_PATH="$BASE/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi

if [ -e "${BASE}/lib" ]; then
    
    export LD_LIBRARY_PATH="$BASE/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi
