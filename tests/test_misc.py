import os
import shutil
import pytest
import argparse

try:
    from unittest import mock  # python 3.3+
except ImportError:
    import mock  # python 2.6-3.2

from convmgr import misc

def test_createDir():
    testPath = os.path.realpath( 'testDir' )
    if os.path.exists( testPath ):
        shutil.rmtree( testPath )
    assert not os.path.exists( testPath )

    misc.createDir( testPath )
    assert os.path.exists( testPath )
    
    misc.createDir( testPath )
    assert os.path.exists( testPath )
    
    shutil.rmtree( testPath )

def test_setupDirectories( ):
    testDir = 'testDir'
    testPath = os.path.realpath( testDir )
    if os.path.exists( testPath ):
        shutil.rmtree( testPath )
    
    misc.setupDirectories( argparse.Namespace( workPath=testDir, outputDir='output', watchDir='watch' ) )

    assert os.path.exists( testPath )
    assert os.path.exists( os.path.join( testPath, 'output' ) )
    assert os.path.exists( os.path.join( testPath, 'watch' ) )

    shutil.rmtree( testPath )

@mock.patch( 'argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace( workPath='testing', outputDir='output', watchDir='watch' ) )
def test_parseArgs( mock_args ):
    args = misc.parseArgs( )

    assert args.workPath == 'testing'
    assert args.outputDir == 'output'
    assert args.watchDir == 'watch'