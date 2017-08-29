#! /bin/bash

. dist/ansi_color.sh
disable_color

echo "$0" "$@"

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

#--- Configure

echo "travis_fold:start:configure"
printf "$ANSI_YELLOW[GHDL] Configure $ANSI_NOCOLOR\n"

CDIR=$(pwd)
prefix="$CDIR/install-$BLD"
mkdir "$prefix"
mkdir "build-$BLD"
cd "build-$BLD"

case "$BLD" in
    mcode)
	config_opts="" ;;
    llvm)
	config_opts="--with-llvm-config" ;;
    llvm-3.5)
	config_opts="--with-llvm-config=llvm-config-3.5 CXX=clang++" ;;
    llvm-3.8)
	config_opts="--with-llvm-config=llvm-config-3.8 CXX=clang++-3.8" ;;
    docker)
	echo "Check docker container!"
	exit 0;;
    *)
	echo "$ANSI_RED[GHDL - build] Unknown build $BLD $ANSI_NOCOLOR"
	exit 1;;
esac
echo "../configure --prefix=$prefix $config_opts"
../configure "--prefix=$prefix" $config_opts
echo "travis_fold:end:configure"

#--- make

echo "travis_fold:start:make"
travis_time_start
printf "$ANSI_YELLOW[GHDL] Make $ANSI_NOCOLOR\n"
make
travis_time_finish
echo "travis_fold:end:make"

echo "travis_fold:start:install"
printf "$ANSI_YELLOW[GHDL] Install $ANSI_NOCOLOR\n"
make install
cd ..
echo "travis_fold:end:install"

#--- package binary

PKG_NAME="ghdl-$TAG-$BLD-$DIST"

echo "travis_fold:start:tar.bin"
printf "$ANSI_YELLOW[GHDL] Create package ${ANSI_DARKCYAN}${PKG_NAME}.tgz $ANSI_NOCOLOR\n"
tar -zcvf "${PKG_NAME}.tgz" -C "$prefix" .
echo "travis_fold:end:tar.bin"

#--- test

export GHDL="$prefix/bin/ghdl"
if ./dist/travis-ci/runtests.sh $ENABLECOLOR; then
    touch build_ok
fi
