#! /bin/bash

. dist/ansi_color.sh
disable_color

# Stop in case of error
set -e

. dist/travis-ci/travis-utils.sh

rm -f build_ok

# Transform long options to short ones
for arg in "$@"; do
  shift
  case "$arg" in
      "--color"|"-color")   set -- "$@" "-c";;
      "--dist"|"-dist")     set -- "$@" "-d";;
      "--build"|"-build")   set -- "$@" "-b";;
      "--pkg"|"-pkg")       set -- "$@" "-p";;
      "--tag"|"-tag")       set -- "$@" "-t";;
    *) set -- "$@" "$arg"
  esac
done
# Parse args
while getopts ":b:d:p:t:c" opt; do
  case $opt in
      c) enable_color;;
      b) BLD=$OPTARG;;
      d) DIST=$OPTARG;;
      p) PKG=$OPTARG;;
      t) TAG=$OPTARG;;
    \?) printf "$ANSI_RED[GHDL] Invalid option: -$OPTARG $ANSI_NOCOLOR\n" >&2
	exit 1 ;;
    :)  printf "$ANSI_RED[GHDL] Option -$OPTARG requires an argument. $ANSI_NOCOLOR\n" >&2
	exit 1 ;;
  esac
done

#--- Env

echo "travis_fold:start:env.docker"
printf "$ANSI_YELLOW[Info] Environment $ANSI_NOCOLOR\n"
env
echo "travis_fold:end:env.docker"


#--- Create source package

echo "travis_fold:start:gpl.src"
printf "$ANSI_YELLOW[Source] create GPL sources $ANSI_NOCOLOR\n"
VER=`echo $TAG | sed -e s/-/./g` # dash is not allowed in debian version
PKG_DIR="ghdl-gpl-$VER"
mv dist/debian .
files=`echo *`
sed -e 's/@abs_srcdir@/./g' < Makefile.in > Makefile.tmp
make -f Makefile.tmp clean-pure-gpl
rm -f Makefile.tmp
mkdir ${PKG_DIR}
mv $files ${PKG_DIR}
tar -zcf "ghdl-gpl_${VER}.orig.tar.gz" ${PKG_DIR}
ls -l
echo "travis_fold:end:gpl.src"


#--- Build package

echo "travis_fold:start:build"
echo "$ANSI_YELLOW[GHDL] Build package $ANSO_NOCOLOR"
cd $PKG_DIR
dpkg-buildpackage -us -uc
echo "travis_fold:end:build"


#--- Install package

echo "travis_fold:start:install"
echo "$ANSI_YELLOW[GHDL] Install package $ANSI_NOCOLOR"
sudo dpkg -i ../*.deb
echo "travis_fold:end:install"

#--- test

export GHDL=ghdl
export GHDL="$prefix/bin/ghdl"
if ./dist/travis-ci/runtests.sh $ENABLECOLOR; then
    touch build_ok
fi
