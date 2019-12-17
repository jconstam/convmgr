import os
import pytest

from convmgr import *

def test_createDir():
    testPath = os.path.realpath( 'testDir' )
    if os.path.exists( testPath ):
        os.rmdir( testPath )
    assert not os.path.exists( testPath )

    # convmgr.createDir( testPath )
    # assert os.path.exists( testPath )
    
    # convmgr.createDir( testPath )
    # assert os.path.exists( testPath )
    
    # os.rmdir( testPath )