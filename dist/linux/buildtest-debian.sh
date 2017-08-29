#! /bin/bash

. dist/ansi_color.sh
disable_color

echo "$0" "$@"

# Stop in case of error
set -e

. dist/linux/travis-utils.sh

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
PKG_DIR="ghdl-gpl-$TAG"
mv dist/debian .
files=`echo *`
sed -e 's/@abs_srcdir@/./g' < Makefile.in > Makefile.tmp
make -f Makefile.tmp clean-pure-gpl
rm -f Makefile.tmp
mkdir ${PKG_DIR}
mv $files ${PKG_DIR}
tar -zcf "ghdl-gpl_${TAG}.orig.tar.gz" ${PKG_DIR}
PKG_NAME="${PKG_DIR}-${BLD}"
echo "travis_fold:end:gpl.src"


#--- Build package

echo "travis_fold:start:build"
echo "$ANSI_YELLOW[GHDL] Build package $ANSO_NOCOLOR"
cd $PKG_DIR
debuild -us -uc
echo "travis_fold:end:build"


#--- Install package

echo "travis_fold:start:install"
echo "$ANSI_YELLOW[GHDL] Install package $ANSI_NOCOLOR"
sudo dpkg -i ../*.deb
echo "travis_fold:end:install"

#--- test

export GHDL=ghdl
cd testsuite
failures=""

echo "travis_fold:start:tests.sanity"
travis_time_start
printf "$ANSI_YELLOW[Test] sanity $ANSI_NOCOLOR\n"
cd sanity
for d in [0-9]*; do
    cd $d
    if ./testsuite.sh > test.log 2>&1 ; then
	echo "sanity $d: ok"
	# Don't disp log
    else
	echo "${ANSI_RED}sanity $d: failed${ANSI_NOCOLOR}"
	cat test.log
	failures="$failures $d"
    fi
    cd ..
    # Stop at the first failure
    [ "$failures" = "" ] || break
done
cd ..
travis_time_finish
echo "travis_fold:end:tests.sanity"
[ "$failures" = "" ] || exit 1

if [ "$ISGPL" != "true" ]; then
    echo "travis_fold:start:tests.gna"
    travis_time_start
    printf "$ANSI_YELLOW[Test] gna $ANSI_NOCOLOR\n"
    cd gna
    dirs=`./testsuite.sh --list-tests`
    for d in $dirs; do
	cd $d
	if ./testsuite.sh > test.log 2>&1 ; then
	    echo "gna $d: ok"
	    # Don't disp log
	else
	    echo "${ANSI_RED}gna $d: failed${ANSI_NOCOLOR}"
	    cat test.log
	    failures="$failures $d"
	fi
	cd ..
	# Stop at the first failure
	[ "$failures" = "" ] || break
    done
    cd ..
    travis_time_finish
    echo "travis_fold:end:tests.gna"
    [ "$failures" = "" ] || exit 1
fi

echo "travis_fold:start:tests.vests"
travis_time_start
printf "$ANSI_YELLOW[Test] vests $ANSI_NOCOLOR\n"
cd vests
if ./testsuite.sh > vests.log 2>&1 ; then
    echo "${ANSI_GREEN}Vests is OK$ANSI_NOCOLOR"
    wc -l vests.log
else
    cat vests.log
    echo "${ANSI_RED}Vests failure$ANSI_NOCOLOR"
    failures=vests
fi
cd ..
travis_time_finish
echo "travis_fold:end:tests.vests"
[ "$failures" = "" ] || exit 1

$GHDL --version
cd ..

#---

echo "[SUCCESSFUL]"
touch build_ok
