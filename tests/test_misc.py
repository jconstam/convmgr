import os
import shutil
import pytest
import argparse

try:
    from unittest import mock  # python 3.3+
except ImportError:
    import mock  # python 2.6-3.2

from convmgr import misc
from tests import common

def setup_function( ):
    common.setupRoot( )
def teardown_function( ):
    common.cleanupRoot( )

def test_createDir():
    testPath = common.createTestPath( 'testDir' )
    common.cleanupPath( testPath )

    misc.createDir( testPath )
    assert os.path.exists( testPath )
    
    misc.createDir( testPath )
    assert os.path.exists( testPath )

def test_setupDirectories( ):
    testPath = common.createTestPath( 'testDir' )
    common.cleanupPath( testPath )
    
    misc.setupDirectories( argparse.Namespace( workPath=testPath, outputDir='output', watchDir='watch' ) )

    assert os.path.exists( testPath )
    assert os.path.exists( os.path.join( testPath, 'output' ) )
    assert os.path.exists( os.path.join( testPath, 'watch' ) )

@mock.patch( 'argparse.ArgumentParser.parse_args', return_value=argparse.Namespace( workPath='testing', outputDir='output', watchDir='watch' ) )
def test_parseArgs( mock_args ):
    args = misc.parseArgs( )

    assert args.workPath == 'testing'
    assert args.outputDir == 'output'
    assert args.watchDir == 'watch'
