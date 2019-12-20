#!/usr/bin/python3

import os
import json
import shutil
import pytest

from convmgr import config
from tests import common

def setup_function( ):
    common.setupRoot( )
def teardown_function( ):
    common.cleanupRoot( )

@pytest.fixture
def testData( ):
    return config.convmgrconfig( common.rootPath )

def test_constructor( testData ):
    assert testData.filePath == common.createTestPath( config.convmgrconfig.fileName )
    assert not testData.data

@pytest.mark.parametrize( 'fileName', [ config.convmgrconfig.fileName, 'file1.json', 'file2' ] )
def test_readFile( testData, fileName ):
    with open( common.createTestPath( fileName ), 'w+' ) as json_file:
        json.dump( { 'testKey1': 'testValue1', 'testKey2': 4 }, json_file )
    
    testData.readFile( )
    if config.convmgrconfig.fileName == fileName:
        assert 'testKey1' in testData.data
        assert testData.getValue( 'testKey1' ) == 'testValue1'
        assert 'testKey2' in testData.data
        assert testData.getValue( 'testKey2' ) == 4
        assert not 'testKey3' in testData.data
        assert testData.getValue( 'testKey3' ) == ''
    else:
        assert not 'testKey1' in testData.data
        assert not 'testKey2' in testData.data
        assert not 'testKey3' in testData.data
    