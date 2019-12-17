import os
import pytest

from convmgr import misc

def test_createDir():
    testPath = os.path.realpath( 'testDir' )
    if os.path.exists( testPath ):
        os.rmdir( testPath )
    assert not os.path.exists( testPath )

    misc.createDir( testPath )
    assert os.path.exists( testPath )
    
    misc.createDir( testPath )
    assert os.path.exists( testPath )
    
    os.rmdir( testPath )