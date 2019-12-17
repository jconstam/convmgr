#!/bin/bash

TEST_PATH="Testing"

#######################

rm -rf $TEST_PATH

#######################

python3 convmgr.py 2&> /dev/null
echo $? > /dev/null
test $? -eq 0 && echo "001 - PASS" || echo "001 - FAIL"

#######################

python3 convmgr.py --workPath $TEST_PATH 2&> /dev/null
echo $? > /dev/null
test $? -eq 0 && echo "002 - PASS" || echo "002 - FAIL"
test -d $TEST_PATH && echo "003 - PASS" || echo "003 - FAIL"
test -d $TEST_PATH/Input && echo "004 - PASS" || echo "004 - FAIL"
test -d $TEST_PATH/Output && echo "005 - PASS" || echo "005 - FAIL"
test -d $TEST_PATH/Output && echo "006 - PASS" || echo "006 - FAIL"

#######################

rm -rf $TEST_PATH

#######################